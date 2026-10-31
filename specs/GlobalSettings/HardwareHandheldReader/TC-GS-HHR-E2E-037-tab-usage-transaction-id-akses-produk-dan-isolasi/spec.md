---
id: TC-GS-HHR-E2E-037-tab-usage-transaction-id-akses-produk-dan-isolasi
title: "Tab Usage: Transaction ID sebagai Tautan atau Teks Biasa Menurut Akses Produk, Strip untuk Event Global Settings, dan Isolasi Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-179
  - TC-GS-HHR-180
  - TC-GS-HHR-181
  - TC-GS-HHR-182
coverage:
  web: automated
---

# Tab Usage: Transaction ID sebagai Tautan atau Teks Biasa Menurut Akses Produk, Strip untuk Event Global Settings, dan Isolasi Client

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai dua akun berurutan lewat langkah ganti akun eksplisit dan hanya membaca data.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A) untuk akun aktor pertama; setelah ganti akun layar dibuka lewat langkah eksplisit.
- Akun yang diuji:

  | Akun | Email | Env var password | Dipakai di | Akses Fixed Asset |
  |---|---|---|---|---|
  | Total Control (Sari Dewi), Client A | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` | TC-GS-HHR-181, 182, 179 (login sekali di hook `before`) | Ada |
  | Read Only (Maya Putri), Client A | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` | TC-GS-HHR-180 (login lewat langkah ganti akun) | Tidak ada |

  Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`) dan Seed Usage Event DD-01 UE-01 sampai UE-06 (fixture baru `Fixture.hardwareHandheldReader.seedUsageDd01`), format tanggal default Client A `dd/MM/yy` 24-hour. DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`) memiliki enam event: tiga event Fixed Asset (`TSK-202606-0014`, `XFER-202606-0007`, `BRW-202606-0031`) dan tiga event Global Settings tanpa transaksi (`Audit TAG`, `Pair TAG`, `Combine TAG`). Client C memiliki reader `SN-HHR-00301` dengan Usage Event sendiri (dipakai sebagai precondition TC-GS-HHR-182, tidak diasersi langsung). Record transaksi audit `TSK-202606-0014` ada di Fixed Asset Client A (disediakan tim FE; lihat Temuan untuk QA). Seed bernama literal tanpa suffix karena asersi bergantung pada nilai seed dan Device Name bawaan ditentukan sistem (HHR-LOGIC-02g); DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1` sehingga baris diidentifikasi lewat Serial Number.
- Cleanup: seed tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme seeding dan pemulihan disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: ganti akun (logout lalu login); membaca apakah teks adalah tautan atau teks biasa; membaca halaman atau record Fixed Asset yang terbuka dari tautan.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite) dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-181: Event Global Settings tanpa transaksi menampilkan strip

1. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
2. Verifikasi tab `Usage` aktif
3. Verifikasi kolom `Transaction ID` baris `Audit TAG` menampilkan `—`
4. Verifikasi kolom `Transaction ID` baris `Pair TAG` menampilkan `—`
5. Verifikasi kolom `Transaction ID` baris `Combine TAG` menampilkan `—`

### TC-GS-HHR-182: Tab Usage tidak menyediakan aksi tulis dan mengikuti isolasi client

6. Verifikasi tidak ada tombol tambah, ubah, atau hapus pada tab
7. Verifikasi tab menampilkan tepat 6 baris event reader DD-01 milik Client A (UE-01 sampai UE-06) tanpa event milik Client C

### TC-GS-HHR-179: Transaction ID menjadi tautan bagi pengguna yang punya akses ke produk

8. Verifikasi teks `TSK-202606-0014` tampil sebagai tautan
9. Klik `TSK-202606-0014`
10. Verifikasi record transaksi audit `TSK-202606-0014` terbuka di Fixed Asset

### Ganti akun ke Read Only

11. Logout dari akun Total Control
12. Login sebagai Read Only (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_RO_PASSWORD`
13. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-180: Transaction ID teks biasa bagi pengguna tanpa akses ke produk

14. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
15. Verifikasi tab `Usage` aktif
16. Verifikasi event Fixed Asset tampil lengkap (6 baris)
17. Verifikasi `TSK-202606-0014` tampil sebagai teks biasa
18. Klik teks `TSK-202606-0014`
19. Verifikasi `TSK-202606-0014` tidak dapat diklik: tidak ada navigasi dan popup tetap terbuka

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 181, 182, 179, 180. Urutan menyimpang dari urutan TC sumber: bagian akun Total Control dijalankan dulu (pengamatan tanpa navigasi, lalu 179 yang membuka record Fixed Asset), kemudian ganti akun ke Read Only untuk 180. Langkah ganti akun (langkah 11 sampai 13) eksplisit; bagian sesudah ganti akun tetap bermakna bila bagian sebelumnya gagal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 sampai 13 (ganti akun dan membuka layar Handheld Reader pada sesi Read Only).
- Langkah 2 dan 15 (`Pastikan Tab Usage aktif` pada Langkah TC) ditulis sebagai `Verifikasi` tab `Usage` aktif.
- Langkah 7 mengasersi isolasi client lewat daftar tepat 6 baris UE-01 sampai UE-06: ciri event Client C tidak disebut TC, sehingga ketiadaan event Client C diasersi sebagai ketiadaan baris selain enam baris itu.
- Spec ini sengaja menggabungkan dua akun karena langkahnya berbeda per akun dan ada Step ganti akun eksplisit (konvensi bagian 3, pemisah nyata kasus b); bukan spec Role Matrix.
- Pembagian TC lintas spec: TC-GS-HHR-169 sampai 178 dan 183 ada di spec 036; TC-GS-HHR-185 dan 186 ada di spec 038.
- Temuan untuk QA:
  - TC-GS-HHR-179 Expected b ("membuka record transaksi audit tersebut di Fixed Asset") tidak menyebut apakah record terbuka di tab baru atau lewat navigasi di tab yang sama, dan tidak menyebut seed task audit `TSK-202606-0014` di Fixed Asset pada Precondition; spec mengasersi record terbuka di Fixed Asset tanpa menentukan cara pembukaan, dan seed task audit dicatat sebagai kebutuhan yang disediakan tim FE.
  - TC-GS-HHR-182 Expected b ("tidak ada event milik Client C") tidak menyebut ciri event Client C (Transaction ID, Event Type); spec mengasersi daftar tepat 6 baris UE-01 sampai UE-06.
  - TC-GS-HHR-180 tidak menyebut bagaimana akun Read Only dibuat tanpa akses Fixed Asset; spec mengikuti Precondition d TC (Read Only Client A tidak memiliki akses ke Fixed Asset).
  - Mekanisme seeding Usage Event dan pemulihan Seed Reader A tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.
