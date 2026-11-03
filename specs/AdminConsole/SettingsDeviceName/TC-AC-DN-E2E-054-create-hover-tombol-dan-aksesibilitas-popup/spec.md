---
id: TC-AC-DN-E2E-054-create-hover-tombol-dan-aksesibilitas-popup
title: "Create Device Name: Hover Tombol dan Aksesibilitas Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-110
  - TC-AC-DN-127
coverage:
  web: automated
---

# Create Device Name: Hover Tombol dan Aksesibilitas Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori.
- Data Dinamis: tidak ada; form tidak pernah diisi dan tidak ada record yang dibuat, sehingga tidak ada cleanup.
- Kemampuan teknis: membaca atribut aksesibilitas elemen (label, `aria-required`, `aria-describedby`) dan memeriksa perputaran fokus keyboard `Tab` di dalam popup; disediakan tim FE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-110: Hover pada tombol Submit dan Clear Field menampilkan perubahan state tampilan

1. Klik tombol `+ Device Name` pada toolbar
2. Arahkan kursor ke tombol `[Submit]`
3. Verifikasi tombol `[Submit]` menampilkan state hover yang berbeda dari state normal
4. Arahkan kursor ke tombol `[Clear Field]`
5. Verifikasi tombol `[Clear Field]` menampilkan state hover yang berbeda dari state normal

### TC-AC-DN-127: Accessibility popup Create

6. Klik `[Submit]` tanpa mengisi apa pun
7. Verifikasi error inline wajib diisi tampil pada field Device Name, Measurement, dan Category
8. Verifikasi field Device Name memiliki label yang terbaca screen reader dan atribut aria-required bernilai true
9. Verifikasi field Measurement memiliki label yang terbaca screen reader dan atribut aria-required bernilai true
10. Verifikasi field Category memiliki label yang terbaca screen reader dan atribut aria-required bernilai true
11. Verifikasi field yang berisi error memiliki atribut aria-describedby yang menunjuk ke pesan error inline
12. Tekan `Tab` berulang sampai fokus berputar
13. Verifikasi fokus Tab berputar di dalam popup dan tidak keluar ke halaman di belakangnya
14. Tekan tombol `Esc`
15. Verifikasi popup tertutup

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Kedua TC bertanda FE Test "UI Only".
- Satu pembukaan popup (langkah 1) dipakai untuk kedua TC karena TC-AC-DN-110 hanya mengamati hover tanpa mengubah form (prinsip 13, "Halaman yang sama dipakai berulang"); popup ditutup pada langkah 14 dengan form kosong (hanya berisi error inline) sehingga tidak ada dialog `Unsaved Changes`.
- Langkah 7 mengasersi error inline yang disebut sebagai hasil langkah TC-AC-DN-127 ("error inline tampil"), sebagai anchor positif untuk asersi atribut pada langkah 11 (S-03).
- Langkah 12 (Tab berulang) adalah aksi tanpa `Verifikasi`; hasil perputaran fokus diasersi pada langkah 13.
- TC-AC-DN-108 dan TC-AC-DN-109 ada di spec 051.
- Temuan untuk QA:
  - TC-AC-DN-110 tidak mendefinisikan wujud "state hover yang berbeda" (warna, bayangan, kursor); asersi hanya membandingkan dengan state normal.
  - TC-AC-DN-127 tidak menyebut berapa kali `Tab` ditekan; spec menekan sampai fokus kembali ke elemen awal.
