import React from 'react'
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Image,
  Button,
  ButtonGroup,
  Slider,
  Select,
  SelectItem
} from '@nextui-org/react'
import { VT323 } from 'next/font/google'

const inter = VT323({
  weight: '400',
  variable: '--font-vt323',
  subsets: ['latin']
})
const places = [
    {label: "Kuchnia", value: "kuchnia", description: "Najpopularniejsze miejsce w biurze"},
    {label: "Taras", value: "taras", description: "Ochota na chiwlę relaksu?"},
    {label: "Piłkarzyki", value: "piłkarzyki", description: "Pora zagrać o prawdziwe stawki!"},
    {label: "Brak", value: "brak", description: "Nie mam preferencji"},

  ];
  const metodyka = [
    {label: "Pomodoro", value: "pomodoro", description: "Najpopularniejsze miejsce w biurze"},
    {label: "Bez przerwy", value: "bez przerwy", description: "Ochota na chiwlę relaksu?"},
    {label: "Brak", value: "brak", description: "Nie mam preferencji"},

  ];
export default function Form () {
  return (
    <div
      className={` ${inter.variable} font-sans flex flex-col w-full p-1 gap-14`}
    >
    <div className='flex flex-col w-full divide-y-4'>
        <p className='flex justify-center text-3xl'> W czasie przerwy</p>
    <div className='flex flex-col w-full gap-8'>
    <Slider
        size='md'
        step={1}
        color='foreground'
        label='Ochota na socjalizowanie'
        radius='none'
        showSteps={true}
        maxValue={5}
        minValue={1}
        defaultValue={3}
        classNames={{
          label: 'text-2xl',
          value: 'text-2xl'
        }}
      />
      <Slider
        size='md'
        step={1}
        color='foreground'
        label='Ochota na aktywne spędzanie przerwy'
        radius='none'
        showSteps={true}
        maxValue={5}
        minValue={1}
        defaultValue={3}
        classNames={{
          label: 'text-2xl',
          value: 'text-2xl'
        }}
      />
      <Select
        label='Preferowane Miejsce'
        placeholder='Wybierz miejsce'
        labelPlacement='outside'
        size='lg'
        className=''
        classNames={{
            "label":"text-2xl",
            "value":"text-xl",
            "listbox":`${inter.variable} font-sans `,
            "mainWrapper":"rounded-none",
            "innerWrapper":"rounded-none",
            "trigger":"rounded-none border-4 border-violet-300",
        }}
      >
        {places.map(place => (
          <SelectItem key={place.value} value={place.value}>
            {place.label}
          </SelectItem>
        ))}
      </Select>
    </div>
    </div>
    <div className='flex flex-col w-full divide-y-4'>
        <p className='flex justify-center text-3xl'> Zaplanuj prace</p>
    <div className='flex flex-col w-full gap-8'>
     
      <Slider
        size='md'
        step={1}
        color='foreground'
        label='Planowane dni pracy stacjonarnie'
        radius='none'
        showSteps={true}
        maxValue={5}
        minValue={2}
        defaultValue={3}
        classNames={{
          label: 'text-2xl',
          value: 'text-2xl'
        }}
      />
      <Select
        label='Preferowana metoda'
        placeholder='Wybierz metodę'
        labelPlacement='outside'
        size='lg'
        className=''
        classNames={{
            "label":"text-2xl",
            "value":"text-xl",
            "listbox":`${inter.variable} font-sans `,
            "mainWrapper":"rounded-none",
            "innerWrapper":"rounded-none",
            "trigger":"rounded-none border-4 border-violet-300",
        }}
      >
        {metodyka.map(place => (
          <SelectItem key={place.value} value={place.value}>
            {place.label}
          </SelectItem>
        ))}
      </Select>
      </div>
      </div>
    </div>
  )
}
