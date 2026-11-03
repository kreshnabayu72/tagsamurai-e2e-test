---
id: TC-AC-ACAL-E2E-022-isi-kolom-tab-session-nilai-kosong-ip-dan-device
title: "Isi Kolom Tab Session: Plain Text, Nilai Kosong, IP, dan Device"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-44
  - TC-AC-ACAL-45
  - TC-AC-ACAL-46
  - TC-AC-ACAL-47
coverage:
  web: automated
---

# Isi Kolom Tab Session: Plain Text, Nilai Kosong, IP, dan Device

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Password subjek dinamis bersuffix (`Agen Kosong {runId}-022`, `Agen Tanpa-IP {runId}-022`) yang dibuat dan dipakai lewat sesi API di hook `before`: `Spectra.env.AC_DYN_PASSWORD` (password uji ditetapkan tim FE; nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`).
- Data Pre-setup (Pre-setup No 9 dan 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus): `John Doe` (EMP001, Staff, Marketing), `Jane Smith` (EMP002, tanpa Position, Finance), `Ani` (tanpa Employee ID).
- Data Dinamis (sufiks `{runId}-022`, `{runId}` hanya digit): dua subjek `Agen Kosong {runId}-022` (tampil `Agen K`) dan `Agen Tanpa-IP {runId}-022` (tampil `Agen T`) dengan Division terisi; Position, Employee ID, dan Division tidak diasersi.
- Data log (entri Session; seed BE, entri terbaru di antara entri subjek yang sama):

  | Kode | User | Employee ID | Position | Division | Note | IP Address | Device / Browser | Cara |
  |---|---|---|---|---|---|---|---|---|
  | e1 | `John Doe` (`John D`) | `EMP001` | `Staff` | `Marketing` | `Session started` | `192.0.2.10` | `Chrome on Windows` | Seed BE |
  | e2 | `John Doe` (`John D`) | `EMP001` | `Staff` | `Marketing` | `Session ended` | `192.0.2.10` | `Chrome on Windows` | Seed BE |
  | e3 | `Jane Smith` (`Jane S`) | `EMP002` | `—` | `Finance` | `Session ended` | `2001:db8::1a` | `Safari on macOS` | Seed BE |
  | e4 | `Agen Kosong {runId}-022` | tidak diasersi | tidak diasersi | terisi | `Session started` | terisi | tidak terparse | Aksi buka Admin Console dari klien tanpa User-Agent standar |
  | e5 | `Ani` | `—` | tidak diasersi | terisi | `Session started` | terisi | terisi | Seed BE |
  | e6 | `Agen Tanpa-IP {runId}-022` | tidak diasersi | tidak diasersi | terisi | `Session started` | tanpa alamat IP | terisi | Seed BE |

- Data uji TC-AC-ACAL-44 (baris amatan; kolom Position hanya diasersi pada baris yang bernilai selain `-`):

  | Kode | Kata Search | Note | IP Address | Device / Browser | Position tampil |
  |---|---|---|---|---|---|
  | e1 | `John Doe` | `Session started` | `192.0.2.10` | `Chrome on Windows` | `-` |
  | e2 | `John Doe` | `Session ended` | `192.0.2.10` | `Chrome on Windows` | `-` |
  | e3 | `Jane Smith` | `Session ended` | `2001:db8::1a` | `Safari on macOS` | `—` |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dengan IP Address, Device / Browser, dan tanpa alamat IP seperti pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); sesi API yang membuka Admin Console tanpa User-Agent standar untuk e4; menelusuri halaman bila baris subjek tidak berada di halaman pertama.
- Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot. Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus dua subjek bersuffix lewat API.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACAL-44: Plain text, IP, dan Device baris Session

1. Verifikasi tabel menampilkan sedikitnya satu baris
2. Untuk setiap baris tabel Data uji TC-AC-ACAL-44 (langkah 2 sampai 8): ketik Search kata Search, tekan Enter
3. Verifikasi baris dengan Note dan IP Address pada tabel menampilkan Activity `Session`, Status `—`, dan Note sesuai tabel
4. Verifikasi Activity dan Status baris itu tampil sebagai plain text, tanpa badge pada Activity maupun Status
5. Verifikasi IP Address baris itu sesuai tabel apa adanya
6. Verifikasi Device / Browser baris itu sesuai tabel
7. Verifikasi Position baris itu tampil `—` (baris bertanda `-` dilewati)
8. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-45: Device / Browser tidak terparse

9. Ketik Search `Agen Kosong {runId}-022`, tekan Enter
10. Verifikasi sel Device / Browser baris `Agen K` tampil `—`
11. Verifikasi sel Device / Browser itu tidak kosong
12. Verifikasi sel Device / Browser itu tidak berisi `null` atau `undefined`
13. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-46: Position kosong

14. Ketik Search `Jane Smith`, tekan Enter
15. Verifikasi sel Position baris `Jane S` tampil `—`
16. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-47: Employee ID dan IP Address kosong, Division dan Note selalu terisi

17. Ketik Search `Ani`, tekan Enter
18. Verifikasi sel Employee ID baris `Ani` tampil `—`
19. Ganti isi kotak search dengan `Agen Tanpa-IP {runId}-022`, tekan Enter
20. Verifikasi sel IP Address baris `Agen T` tampil `—`
21. Verifikasi sel IP Address itu tidak kosong
22. Verifikasi sel IP Address itu tidak berisi `null`
23. Klik `✕` pada Search, tekan Enter
24. Verifikasi tabel menampilkan sedikitnya satu baris
25. Verifikasi sel Division terisi (tidak `—`) di semua baris halaman yang tampil
26. Verifikasi sel Note terisi (tidak `—`) di semua baris halaman yang tampil

### Pemulihan state

27. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4a, Tab Session). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search nama subjek untuk menemukan baris amatan di tabel audit trail yang tumbuh (langkah 2, 9, 14, 17, 19, S-14), pengosongan Search (langkah 8, 13, 16, 23), dan penutupan Search di langkah 27 (hook `after` sebagai cadangan). Halaman Session sudah dibuka hook `beforeEach` suite sehingga spec tidak membuka ulang. Langkah 1 dan 24 adalah pembanding generik sebelum asersi.
- Langkah 2 sampai 8 berulang untuk setiap baris tabel Data uji TC-AC-ACAL-44 (tiga iterasi).
- Spec memiliki 27 langkah nominal dan 41 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (isi kolom Tab Session pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari satu perulangan per baris data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri Session (IP Address, Device / Browser, entri tanpa IP) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-44 Expected d (Position `Jane S` tampil `—`) sama dengan TC-AC-ACAL-46; spec mengasersinya di kedua blok.
  - TC-AC-ACAL-45 menyebut "buka AC dari client tanpa User-Agent standar" tanpa subjek; spec memakai subjek bersuffix `Agen Kosong {runId}-022` dan sesi API tanpa User-Agent standar. Subjek untuk TC-AC-ACAL-47 (entri tanpa IP) juga tidak disebut; spec memakai `Agen Tanpa-IP {runId}-022`.
  - TC-AC-ACAL-47 Expected b menyebut "semua baris" Division dan Note; spec mengasersinya pada baris halaman yang tampil, bukan seluruh audit trail.
  - TC-AC-ACAL-44 mencantumkan Position `Staff` untuk `John Doe` tetapi tidak mengasersinya; tidak diasersi.
