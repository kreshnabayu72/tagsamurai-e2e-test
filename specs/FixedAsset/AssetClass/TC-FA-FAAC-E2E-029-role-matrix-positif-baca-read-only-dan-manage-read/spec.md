---
id: TC-FA-FAAC-E2E-029-role-matrix-positif-baca-read-only-dan-manage-read
title: "Role Matrix Positif: Read Only dan Manage Accounting (Read) Dapat Mencari, Memfilter, Mengunduh, Membuka Changelog, dan Membuka Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-73
  - TC-FA-FAAC-74
coverage:
  web: automated
---

# Role Matrix Positif: Read Only dan Manage Accounting (Read) Dapat Mencari, Memfilter, Mengunduh, Membuka Changelog, dan Membuka Detail

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Read Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-73 |
| Manage accounting (Read) | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_R_PASSWORD` | TC-FA-FAAC-74 |

- Env var: `FA_AC_RO_PASSWORD`, `FA_AC_MA_R_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. Dibaca, tidak diubah.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite). Unduhan berkas tidak mengubah data.
- Kemampuan teknis: ganti akun (logout lalu login), membaca daftar berkas yang terunduh (nama berkas), Search dengan Enter.

## Test Steps

### TC-FA-FAAC-73

1. Verifikasi sedikitnya satu baris pada tabel Asset Class tampil
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Verifikasi baris HEAVY-EQ tampil di tabel
4. Klik icon Filter
5. Verifikasi panel Filter terbuka
6. Tutup panel Filter (Esc)
7. Klik icon Download, lalu pilih Download as CSV
8. Verifikasi berkas Asset-Class.csv terunduh
9. Klik icon Changelog
10. Verifikasi modal "Changelog: Asset Class" terbuka
11. Tutup modal Changelog
12. Klik Class Code HEAVY-EQ
13. Verifikasi halaman Detail HEAVY-EQ terbuka
14. Verifikasi semua tab pada Detail HEAVY-EQ dapat dilihat

### TC-FA-FAAC-74

15. Ganti akun: logout, lalu login sebagai Manage accounting (Read)
16. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
17. Klik icon Changelog
18. Verifikasi modal "Changelog: Asset Class" terbuka
19. Tutup modal Changelog
20. Klik icon Download, lalu pilih Download as XLSX
21. Verifikasi berkas Asset-Class.xlsx terunduh
22. Ketik Search `VEHICLES`, tekan Enter
23. Klik Class Code VEHICLES
24. Verifikasi halaman Detail VEHICLES terbuka

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec Role Matrix positif (bagian 3a): aksi baca tersedia bagi role yang hanya berhak baca.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 11, dan 19 (menutup panel atau modal, S-09), langkah 15 (ganti akun), langkah 16 (membuka tab Asset Class sesudah login ulang, S-07).
- Search `HEAVY-EQ` pada langkah 2 tidak dikosongkan sebelum langkah 12: TC mengklik Class Code HEAVY-EQ pada hasil Search yang sama, sehingga baris itu tampil tanpa bergantung pada halaman 1.
- Search ke `HEAVY-EQ` di langkah TC-FA-FAAC-73 adalah objek uji; `Verifikasi` sedikitnya satu baris tampil (langkah 1) mendahului Search sebagai pembanding, dan langkah 3 mengasersi baris HEAVY-EQ ada (bukan "hanya") karena Class Name searchable sehingga baris seed lain, mis. `B-ANCHOR` "Anchor Heavy Equipment", dapat ikut tampil.
- Nama berkas Asset-Class.csv dan Asset-Class.xlsx diasersi sebagai nama berkas (asersi fungsional); isi berkas tidak diasersi karena TC tidak memintanya.
- Temuan untuk QA:
  - TC-FA-FAAC-73 langkah 2 menyebut "lalu buka panel" tanpa menyebut isi panel; spec hanya mengasersi panel Filter terbuka sesuai Expected.
  - TC-FA-FAAC-73 Expected e menyebut "semua tab dapat dilihat" tanpa daftar tab; spec mengasersi tab pada Detail dapat dilihat tanpa menyebut nama tab.
