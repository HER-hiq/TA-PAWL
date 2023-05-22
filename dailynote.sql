-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 22 Bulan Mei 2023 pada 18.16
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dailynote`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `activity`
--

CREATE TABLE `activity` (
  `no` int(11) NOT NULL,
  `jenis_kegiatan` varchar(10) NOT NULL,
  `keterangan` varchar(100) NOT NULL,
  `tanggal` date NOT NULL,
  `waktu` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `activity`
--

INSERT INTO `activity` (`no`, `jenis_kegiatan`, `keterangan`, `tanggal`, `waktu`) VALUES
(4, 'Tugas', 'Kerja Bakti', '2023-04-04', '08:00:00'),
(7, 'Rutin', 'Belajar', '2023-04-10', '16:26:00'),
(8, 'Rutin', 'Taraweh', '2023-04-19', '17:30:00');

-- --------------------------------------------------------

--
-- Struktur dari tabel `rencana`
--

CREATE TABLE `rencana` (
  `no` int(11) NOT NULL,
  `aktivitas` text NOT NULL,
  `tanggal` date NOT NULL,
  `waktu` time NOT NULL,
  `prioritas` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `rencana`
--

INSERT INTO `rencana` (`no`, `aktivitas`, `tanggal`, `waktu`, `prioritas`) VALUES
(3, 'mengaji', '2023-05-22', '22:56:00', 'high');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tugas`
--

CREATE TABLE `tugas` (
  `no` int(11) NOT NULL,
  `aktivitas` text NOT NULL,
  `tanggal` date NOT NULL,
  `waktu` time NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tugas`
--

INSERT INTO `tugas` (`no`, `aktivitas`, `tanggal`, `waktu`, `status`) VALUES
(2, ',jgljgcotc fh', '2023-05-31', '22:12:00', 0),
(3, 'hgwdj', '2023-05-24', '00:00:00', 0),
(5, 'hahahahahaa', '2023-05-29', '22:38:00', 0);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `activity`
--
ALTER TABLE `activity`
  ADD PRIMARY KEY (`no`);

--
-- Indeks untuk tabel `rencana`
--
ALTER TABLE `rencana`
  ADD PRIMARY KEY (`no`);

--
-- Indeks untuk tabel `tugas`
--
ALTER TABLE `tugas`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `activity`
--
ALTER TABLE `activity`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `rencana`
--
ALTER TABLE `rencana`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `tugas`
--
ALTER TABLE `tugas`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
