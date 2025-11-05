'use client'

import Link from 'next/link'
import { Button } from '@/components/ui/button'

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8">
      <div className="max-w-2xl text-center space-y-6">
        <h1 className="text-5xl font-bold bg-gradient-to-r from-primary-600 to-blue-600 bg-clip-text text-transparent">
          PhysioCapture
        </h1>
        <p className="text-xl text-gray-600">
          Sistema completo de gestão para clínicas de fisioterapia
        </p>
        <p className="text-gray-500">
          Gerencie pacientes, consultas e documentos de forma eficiente e organizada
        </p>
        <div className="flex gap-4 justify-center pt-4">
          <Link href="/login">
            <Button size="lg">Fazer Login</Button>
          </Link>
          <Link href="/register">
            <Button size="lg" variant="outline">Criar Conta</Button>
          </Link>
        </div>
      </div>
    </main>
  )
}
