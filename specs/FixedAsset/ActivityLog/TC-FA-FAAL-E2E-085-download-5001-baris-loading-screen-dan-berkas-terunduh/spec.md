---
id: TC-FA-FAAL-E2E-085-download-5001-baris-loading-screen-dan-berkas-terunduh
title: "Volume 5.001 Baris: Download Menampilkan Loading Screen lalu Berkas Langsung Terunduh"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-183
coverage:
  web: automated
---

# Volume 5.001 Baris: Download Menampilkan Loading Screen lalu Berkas Langsung Terunduh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client volume (Pre-setup #14). Email dan nama env var password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data (kelas e, volume data): client dengan volume tepat 5.001 baris Tab Session dan 5.001 baris Tab User Action (Pre-setup #14). Seed volume disediakan tim FE/BE dan dimiliki spec ini (S-06).
- Kemampuan teknis: penangkap unduhan browser dan parser CSV (butir "Kemampuan teknis tambahan" di `suite.md`); kemampuan membaca jumlah notifikasi in-app dan jumlah job background sebelum dan sesudah aksi, disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-183: Download 5.001 baris menampilkan loading screen lalu berkas langsung terunduh (Tab Session)

1. Catat jumlah notifikasi in-app dan jumlah job background sebagai baseline
2. Klik icon Download di Tab Session
3. Pilih `Download as CSV`
4. Verifikasi loading screen tampil pada Tab Session
5. Verifikasi tidak ada toast informasional pada Tab Session
6. Verifikasi berkas langsung terunduh pada Tab Session
7. Verifikasi berkas memuat 5.001 baris data pada Tab Session

### TC-FA-FAAL-183: Download 5.001 baris menampilkan loading screen lalu berkas langsung terunduh (Tab User Action)

8. Klik tab User Action
9. Klik icon Download di Tab User Action
10. Pilih `Download as CSV`
11. Verifikasi loading screen tampil pada Tab User Action
12. Verifikasi tidak ada toast informasional pada Tab User Action
13. Verifikasi berkas langsung terunduh pada Tab User Action
14. Verifikasi berkas memuat 5.001 baris data pada Tab User Action
15. Buka pusat notifikasi
16. Verifikasi pusat notifikasi terbuka
17. Verifikasi tidak ada notifikasi in-app baru dibanding baseline
18. Verifikasi tidak ada job background baru dibanding baseline

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 1 (mencatat baseline notifikasi dan job sebelum aksi).
- Asersi absence state sementara (bagian 8b butir 11): `Verifikasi` tidak ada toast diletakkan segera setelah pemicu (pilih `Download as CSV`), sebelum `Verifikasi` berkas terunduh. Loading screen yang tampil menjadi anchor positif untuk absence toast.
- Temuan untuk QA:
  - Pre-setup #14 tidak menyebut client dan akun aktor untuk volume 5.001 baris. Login aktor mencatat baris Session baru sehingga volume "tepat 5.001" dapat bergeser; spec mengikuti angka TC dan menyerahkan penyesuaian seed ke tim FE/BE.
  - TC-FA-FAAL-183 langkah 4 ("Periksa pusat notifikasi dan daftar job") tidak menyebut lokasi UI pusat notifikasi dan sumber daftar job; spec memakai baseline jumlah notifikasi dan job yang dibaca lewat kemampuan tim FE/BE.
  - TC-FA-FAAL-183 hanya mengasersi jumlah baris berkas; isi berkas (nilai sel) bukan objek spec ini.
