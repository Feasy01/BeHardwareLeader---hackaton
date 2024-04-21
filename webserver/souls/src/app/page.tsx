'use client'
import React from 'react'
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
  User,
  Chip,
  Tooltip,
  ChipProps,
  getKeyValue,
  Image
} from '@nextui-org/react'
import { EditIcon } from './EditIcon.jsx'
import { DeleteIcon } from './DeleteIcon.jsx'
import { EyeIcon } from './EyeIcon.jsx'
import  Navbar from "./(views)/navabr"
import Soul from "./(views)/yoursoul"
import SportsSoccerIcon from '@mui/icons-material/SportsSoccer';
import { VT323 } from "next/font/google";
import Zdjecie from './(views)/zdj/default.png'
import Zdjecie2 from './(views)/zdj/default2.png'
import 'sockjs-client'
const statusColorMap: Record<string, ChipProps['color']> = {
  active: 'success',
  paused: 'danger',
  vacation: 'warning'
}
const columns = [
  { name: 'IMIE', uid: 'name' },
  { name: 'OUTFIT', uid: 'outfit' },
  { name: 'PUNKTY', uid: 'points' },
  { name: 'AKCJE', uid: 'actions' }

]
const zdj = [Zdjecie,Zdjecie2]

const inter = VT323({weight:"400",
  variable:"--font-vt323",
  subsets:["latin"]
})
export default function App () {
  const [clients, setClients] = React.useState([
 
  ])

  React.useEffect(() => {
    const socket = new WebSocket('ws://localhost:7890/') // Connect to your server
    socket.onopen = event => {
      socket.send(JSON.stringify({ type: 'get_users' }))
    }
    socket.addEventListener('message', event => {
      const serverResponse = event.data
      const parsedResponse = JSON.parse(serverResponse)
      if (parsedResponse['type'] === 'get_users') {
        setClients(parsedResponse['data'])
      }
    })
    // socket.on('connect', () => {
    //     console.log('Connected to WebSocket server');
    // });

    // socket.on('message_from_server', (data) => {
    //     console.log('Received from server:', data);
    // });

    return () => socket.close()
  }, [])

  const renderCell = React.useCallback((user, columnKey: React.Key) => {
    const cellValue = user[columnKey]

    switch (columnKey) {
      case 'name':
        return (
          <User
            classNames={{"name":"text-xl"}}
            avatarProps={{ radius: 'lg', src: user.avatar,size:"lg" ,className:"text-2xl"}}
            description={user.email}
            name={cellValue}
          >
            {user.email}
          </User>
        )
      case 'rf_id':
        return (
          <div className='flex flex-col text-xl'>
            <p className='text-bold text-lg capitalize'>{cellValue}</p>
            <p className='text-bold text-lg capitalize text-default-400'>
              {user.team}
            </p>
          </div>
        )
      case 'outfit':
        return (
          
          <Image
          alt='Card background'
          className='object-cover rounded-xl'
          src={zdj[cellValue-1].src}
          width={400}
        />
        )
      case 'points':
        return (
          <Chip
            className='capitalize'
            classNames={{"content":"text-xl"}}
            color={statusColorMap[user.status]}
            size='lg'
            variant='flat'
          >
            {cellValue}
          </Chip>
        )
      case 'actions':
          return (
            <div className='relative flex items-center gap-2'>
              <Tooltip content='Wyzwij na mecz w piłkarzyki'>
                <span className='text-lg text-default-400 cursor-pointer active:opacity-50'>
                  <SportsSoccerIcon />
                </span>
              </Tooltip>
            </div>
          )
      default:
        return cellValue
    }
  }, [clients])

  return (
    <div className={`${inter.variable} font-sans h-full`}>
    <Navbar/>
    <div className='grid grid-cols-5 grid-rows-5 w-full gap-5 p-10 max-h-[90%]'>
      <Soul/>
      <div className='col-span-1 col-start-5 row-span-5'>
      <Table aria-label='Example table with custom cells' classNames={{
        "base":"h-full ",
        "wrapper":"h-full border-8 border-violet-400 rounded-none"
      }}>
        <TableHeader columns={columns}>
          {column => (
            <TableColumn
              key={column.uid}
              align={column.uid === 'actions' ? 'center' : 'start'}
              className='text-xl'
            >
              {column.name}
            </TableColumn>
          )}
        </TableHeader>
        <TableBody items={clients}>
          {item => (
            <TableRow key={item.rf_id}>
              {columnKey => (
                <TableCell >{renderCell(item, columnKey)}</TableCell>
              )}
            </TableRow>
          )}
        </TableBody>
      </Table>
      </div>
    </div>
    </div>
  )
}
