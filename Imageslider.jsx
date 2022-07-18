import React from 'react'
import './Imageslider.css'
import { Slider } from './SliderData'
import { useState } from 'react'
import { FaArrowAltCircleRight, FaArrowAltCircleLeft } from 'react-icons/fa'

const Imageslider = ({ Slides }) => {
    const [images, setimages] = useState(0)
    const length = Slides.lenght

    const nextslide = ()=> {
        setimages(images === length - 1 ? 0 : images + 1)
    }


    // const prevslide = ()=> {
    //     setimages(images === 0 ? length ? length - 1 : images - 1)
    // }

    // console.log(images)

    if (!Array.isArray(Slides) || Slides.lenght <= 0) {
        return null
    }

    

  return (
    <div className='image'>
        {Slider.map((Slide, index)=> {
            return (
                <img src={Slide.image} alt=""  className='img'/>
                )
        })}
        <div className='pointer'>
            <FaArrowAltCircleLeft className='left-arrow arrow'  />
            <FaArrowAltCircleRight className='right-arrow arrow' onClick={nextslide} />
        </div>
    </div>
  )
}

export default Imageslider