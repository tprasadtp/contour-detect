# Background filter using open cv bindings for pyhon


import cv
import cv2
import numpy as np



def cv2array(im):
  depth2dtype = {
        cv.IPL_DEPTH_8U: 'uint8',
        cv.IPL_DEPTH_8S: 'int8',
        cv.IPL_DEPTH_16U: 'uint16',
        cv.IPL_DEPTH_16S: 'int16',
        cv.IPL_DEPTH_32S: 'int32',
        cv.IPL_DEPTH_32F: 'float32',
        cv.IPL_DEPTH_64F: 'float64',
    }

  a = np.fromstring(
         im.tostring(),
         dtype=depth2dtype[im.depth],
         count=im.width*im.height*im.nChannels)
  a.shape = (im.height,im.width,im.nChannels)
  return a

def array2cv(a):
  dtype2depth = {
        'uint8':   cv.IPL_DEPTH_8U,
        'int8':    cv.IPL_DEPTH_8S,
        'uint16':  cv.IPL_DEPTH_16U,
        'int16':   cv.IPL_DEPTH_16S,
        'int32':   cv.IPL_DEPTH_32S,
        'float32': cv.IPL_DEPTH_32F,
        'float64': cv.IPL_DEPTH_64F,
    }
  try:
    nChannels = a.shape[2]
  except:
    nChannels = 1
  cv_im = cv.CreateImageHeader((a.shape[1],a.shape[0]),
          dtype2depth[str(a.dtype)],
          nChannels)
  cv.SetData(cv_im, a.tostring(),
             a.dtype.itemsize*nChannels*a.shape[1])
  return cv_im

if __name__ == '__main__':
        capture = cv.CaptureFromCAM(0)
        history = 100
        nGauss =3
        bgThresh = 0.6
        noise = 1
        bgs = cv2.BackgroundSubtractorMOG(history,nGauss,bgThresh,noise) #Background Subtractor MOG Construct

        image = cv.QueryFrame(capture)
        cv.ShowImage('Webcam Input',image)

        mat = cv2array(image)	 #Convert to Numpy Array format_1
        format_1 = bgs.apply(mat)	 #Call the Function
        foreground = array2cv(format_1);	 #Convert back to OpenCV format_1

        cv.ShowImage('Foreground',foreground)
        cv.WaitKey(15)

        while (1):
                image = cv.QueryFrame(capture)
                cv.ShowImage('Webcam Input',image)

                mat = cv2array(image)	 #Convert to Numpy Array format_1
                bgs.apply(mat,format_1,-1)	 #Call the Function
                foreground = array2cv(format_1);	 #Convert back to OpenCV format_1

                cv.ShowImage('Foreground',foreground)
                ch = 0xFF & cv2.waitKey(5)
                if ch == 27:
                    break
                    cv.capture.release()
                    cv2.destroyAllWindows()
                    cv.capture.release()
