import React from 'react'
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Image,
  Button,
  ButtonGroup
} from '@nextui-org/react'
import Zdjecie from './zdj/default.png'
import { VT323 } from 'next/font/google'
import Form from "./formularz"
const inter = VT323({weight:"400",
  variable:"--font-vt323",
  subsets:["latin"]
})
export default function Soul () {
  return (
    <div className={` ${inter.variable} font-sans col-span-2 col-start-2 row-start-1 row-span-2 h-full`}>
      <Card className='py-4 border-8 border-violet-400 rounded-none'>
        <CardBody className='grid grid-cols-2 grid-rows-1 gap-5 p-5'>
          <Card className='border-8 border-grey-800 rounded-none'>
            <CardHeader className='pb-0 pt-2 px-4 flex-row w-full justify-center'>
              <h4 className={`${inter.variable} font-sans text-5xl`}>Personalizacja</h4>
            </CardHeader>
            <CardBody>
              <Form/>

            </CardBody>
          </Card>
            <Card className='border-8 border-grey-800  rounded-none'>
              <CardHeader className='pb-0 pt-2 px-4 flex-row w-full justify-center'>
                <h4 className={`${inter.variable} font-sans text-5xl`}>Twój Chad CHECKER</h4>
              </CardHeader>
              <CardBody>
                <Image
                  alt='Card background'
                  className='object-cover rounded-xl'
                  src={Zdjecie.src}
                  width={400}
                />
                <ButtonGroup>
                  <Button className='text-3xl rounded-none'>{`<`}</Button>
                  <Button className='text-3xl rounded-none'>{`>`}</Button>
                </ButtonGroup>
              </CardBody>
            </Card>
        </CardBody>
      </Card>
    </div>
  )
}
