---
id: TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus
title: "Create: nilai khusus, Temporary besok, reuse Email dan Employee ID milik user terhapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-109
  - TC-GS-USER-113
  - TC-GS-USER-115
  - TC-GS-USER-116
  - TC-GS-USER-125
  - TC-GS-USER-138
coverage:
  web: automated
---

# Create: nilai khusus, Temporary besok, reuse Email dan Employee ID milik user terhapus

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Layar awal: hook `beforeEach` mengembalikan layar ke Global Settings > User > User List, sub-tab Login User.
- Data Pre-setup (hanya dibaca, tidak diubah): Division `Finance`, `General Affairs`, `Logistics` (No. 23); Position `HR Business Partner` (No. 22); opsi Access `Fixed Asset`, `Supply Asset`, `Global Settings` (No. 26, Client PT Maju Bersama subscribe Fixed Asset + Supply Asset).
- Data Dinamis, semua bersuffix `{runId}-026`. Kemampuan membuat dan menghapus user lewat API di hook `before` disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD):
  - UT-1 (user terhapus, dibuat lewat API lalu dihapus lewat API di hook `before`): First Name `Rudi`, Last Name `Hakim Lama {runId}-026`, Email `rudihakim+{runId}-026@qwertysystem.net`, Employee ID `EMP-0300-{runId}-026`, Division `Finance`, Access `Fixed Asset`. Dipakai TC-GS-USER-113 (reuse Email) dan TC-GS-USER-116 (reuse Employee ID).
  - Seluruh user yang dibuat lewat UI memakai Division `Finance` dan Access `Fixed Asset` kecuali disebut lain:
    - U-109: First Name `Budi`, Last Name `Santoso 109 {runId}-026`, Email `budisantoso109+{runId}-026@qwertysystem.net`, Employee ID `EMP/2026#01-{runId}-026`.
    - U-113: First Name `Budi`, Last Name `Santoso 113 {runId}-026`, Email `rudihakim+{runId}-026@qwertysystem.net`.
    - U-115: First Name `Budi`, Last Name `Santoso 115 {runId}-026`, Email `budisantoso115+{runId}-026@qwertysystem.net`, Employee ID dikosongkan.
    - U-116: First Name `Budi`, Last Name `Santoso 116 {runId}-026`, Email `budisantoso116+{runId}-026@qwertysystem.net`, Employee ID `EMP-0300-{runId}-026`.
    - U-125: First Name `Budi`, Last Name `Santoso 125 {runId}-026`, Email `budisantoso125+{runId}-026@qwertysystem.net`, Temporary Until = besok.
    - U-138a: First Name `Andre`, Last Name `Kurniawan {runId}-026`, Email `andrekurniawan+{runId}-026@qwertysystem.net`, Division `Logistics`.
    - U-138b: First Name `Maya`, Last Name `Anggraini {runId}-026`, Email `mayaanggraini+{runId}-026@qwertysystem.net`, Division `Finance`, Access `Supply Asset`, Position `HR Business Partner`.
    - U-138c: First Name `Rudi`, Last Name `Hakim 138 {runId}-026`, Email `rudihakim138+{runId}-026@qwertysystem.net`, Division `General Affairs`, Access `Global Settings`.
  - Emergency Phone (No. 24) diisi pada setiap Create mengikuti TC: Country Code `🇮🇩 +62`, Number `81234567890`.
  - Nama tampil di User List: `{First Name} {Last Name}`.
- Tanggal "besok" (TC-GS-USER-125): dihitung dari jam browser pada zona waktu client General Settings (NC-06: Temporary Until adalah hari aktif terakhir). Format tanggal pada Detail mengikuti format tanggal General Settings client.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API UT-1 dan semua user bersuffix `{runId}-026`.
- State global yang diubah: Custom Field `Emergency Phone` tidak Required selama spec ini (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158 dan 349, TC Create dan Edit lain dijalankan saat Required nonaktif). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah. Spec membuat data dan berjalan dalam suite serial; form Create dibuka sekali dengan checkbox `Stay on this form after submitting`.
- Kemampuan teknis (disediakan tim FE/BE bila belum ada): menunggu ±500 ms nyata untuk debounce validasi real-time (jeda pendek, langkah 5, 11, dan 22).

## Test Steps

### Persiapan

1. Klik `[+ User]` di Table Tools
2. Centang `Stay on this form after submitting`

### TC-GS-USER-109: Employee ID boleh memuat karakter di luar whitelist Code/ID

3. Isi First Name `Budi`, Last Name `Santoso 109 {runId}-026`, Division `Finance`, Email `budisantoso109+{runId}-026@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
4. Isi Employee ID `EMP/2026#01-{runId}-026`
5. Tunggu ±500 ms (debounce validasi)
6. Verifikasi tidak ada error `contains invalid characters` di bawah field Employee ID
7. Klik `[Submit]`
8. Verifikasi toast sukses: "Success, user has been created."
9. Tunggu toast sukses hilang otomatis

### TC-GS-USER-113: Email milik user yang sudah dihapus dapat dipakai lagi

10. Isi First Name `Budi`, Last Name `Santoso 113 {runId}-026`, Division `Finance`, Email `rudihakim+{runId}-026@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
11. Tunggu ±500 ms (debounce validasi)
12. Verifikasi tidak ada error `Email already exists` di bawah field Email
13. Klik `[Submit]`
14. Verifikasi toast sukses: "Success, user has been created."
15. Tunggu toast sukses hilang otomatis

### TC-GS-USER-115: Employee ID kosong boleh disimpan dan tidak dicek duplikat

16. Isi First Name `Budi`, Last Name `Santoso 115 {runId}-026`, Division `Finance`, Email `budisantoso115+{runId}-026@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`) (Employee ID dibiarkan kosong)
17. Klik `[Submit]`
18. Verifikasi toast sukses: "Success, user has been created."
19. Tunggu toast sukses hilang otomatis

### TC-GS-USER-116: Employee ID milik user soft-deleted tidak dihitung duplikat

20. Isi First Name `Budi`, Last Name `Santoso 116 {runId}-026`, Division `Finance`, Email `budisantoso116+{runId}-026@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
21. Isi Employee ID `EMP-0300-{runId}-026`
22. Tunggu ±500 ms (debounce validasi)
23. Verifikasi tidak ada error `Employee ID already exists` di bawah field Employee ID
24. Klik `[Submit]`
25. Verifikasi toast sukses: "Success, user has been created."
26. Tunggu toast sukses hilang otomatis

### TC-GS-USER-125: Temporary Until besok diterima

27. Isi First Name `Budi`, Last Name `Santoso 125 {runId}-026`, Division `Finance`, Email `budisantoso125+{runId}-026@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
28. Centang `Set as Temporary User`
29. Pilih Temporary Until = besok
30. Klik `[Submit]`
31. Verifikasi toast sukses: "Success, user has been created."
32. Tunggu toast sukses hilang otomatis

### TC-GS-USER-138: Create beruntun via Stay on this form untuk data populasi

33. Isi First Name `Andre`, Last Name `Kurniawan {runId}-026`, Division `Logistics`, Email `andrekurniawan+{runId}-026@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
34. Klik `[Submit]`
35. Verifikasi toast sukses: "Success, user has been created."
36. Tunggu toast sukses hilang otomatis
37. Isi First Name `Maya`, Last Name `Anggraini {runId}-026`, Division `Finance`, Email `mayaanggraini+{runId}-026@qwertysystem.net`, pilih Access `Supply Asset`, pilih Position `HR Business Partner`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
38. Klik `[Submit]`
39. Verifikasi toast sukses: "Success, user has been created."
40. Tunggu toast sukses hilang otomatis
41. Isi First Name `Rudi`, Last Name `Hakim 138 {runId}-026`, Division `General Affairs`, Email `rudihakim138+{runId}-026@qwertysystem.net`, pilih Access `Global Settings`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
42. Klik `[Submit]`
43. Verifikasi toast sukses: "Success, user has been created."
44. Klik `✕` untuk menutup Popup Create

### Verifikasi hasil di User List

45. Klik icon Search, ketik `{runId}-026`, tekan Enter
46. Verifikasi sel Employee ID baris `Budi Santoso 109 {runId}-026`: `EMP/2026#01-{runId}-026`
47. Verifikasi sel Employee ID baris `Budi Santoso 115 {runId}-026`: `—`
48. Verifikasi baris `Andre Kurniawan {runId}-026` tampil di User List
49. Verifikasi baris `Maya Anggraini {runId}-026` tampil di User List
50. Verifikasi baris `Rudi Hakim 138 {runId}-026` tampil di User List
51. Klik Name `Budi Santoso 125 {runId}-026` untuk membuka Detail
52. Verifikasi Detail menampilkan `Temporary until [tanggal besok]` dengan tanggal besok pada format tanggal General Settings client

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (52 langkah) karena seluruh TC berada di satu kelas (Create sukses dengan nilai khusus), satu layar, dan satu pembukaan form dengan `Stay on this form after submitting` (prinsip 8 bagian 3). Tiap blok memakai data sendiri bersuffix dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Tiga Submit pada TC-GS-USER-138 menyumbang sebelas langkah.
- Pembukaan form (langkah 1 dan 2) dipakai bersama oleh langkah `Klik [+ User]` dan `Centang Stay on this form` pada TC-GS-USER-109, 113, 115, 116, 125, dan 138. Form di-reset oleh Stay on this form antar Submit sehingga Employee ID kembali kosong pada tiap blok.
- Urutan TC sumber: 109, 113, 115, 116, 125, 138 (sama dengan urutan `sourceTc`). Verifikasi sel List (Employee ID TC-GS-USER-109 dan 115, ketiga user TC-GS-USER-138) dan Detail (TC-GS-USER-125) diletakkan sesudah Popup ditutup (langkah 44) karena baru teramati di List setelah Popup tertutup; toast, yang bersifat sementara, diasersi segera sesudah tiap Submit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 44 (menutup Popup, bagian TC-GS-USER-138), 45 (Search untuk mempersempit List ke user spec ini), 51 (membuka Detail untuk TC-GS-USER-125); langkah 5, 11, dan 22 (menunggu debounce validasi ±500 ms sebelum asersi absence error, bagian 8b butir 2 dan 5); langkah 9, 15, 19, 26, 32, 36, dan 40 (menunggu toast sukses sebelumnya hilang supaya toast berikutnya tidak tertukar, R-12).
- Value Employee ID dan Email diberi suffix `{runId}-026` agar unik per run; `EMP/2026#01` tetap memuat `/` dan `#` sebagai karakter di luar whitelist Code/ID. UT-1 dipakai bersama oleh TC-GS-USER-113 dan 116 untuk dua user baru yang berbeda: U-113 memakai Email UT-1, U-116 memakai Employee ID UT-1.
- Pembagian TC: validasi duplikat Email dan Employee ID aktif (inline error) diverifikasi di spec 023; trim spasi di spec 025; Create sukses field wajib dan semua field di spec 024.
- Temuan untuk QA:
  - TC-GS-USER-109, 113, 116: Expected "tidak ada error ..." berupa asersi absence pada validasi real-time; TC tidak menyebut jeda debounce validasi (V-07). Spec menunggu ±500 ms sesudah field terisi dan mengasersi sebelum `[Submit]`.
  - TC-GS-USER-113 dan 116: precondition "User `Rudi Hakim` sudah dihapus" tidak menyebut cara menghapus; spec memakai UT-1 yang dihapus lewat API (disediakan tim FE/BE). TC-GS-USER-113 menyebut Rudi Hakim dengan Email `rudihakim@qwertysystem.net` dan TC-GS-USER-116 menyebut Employee ID `EMP-0300`; UT-1 memuat keduanya.
  - TC-GS-USER-113 langkah 2 "Isi field wajib, Email ..." tidak menyebut nilai field wajib lain; spec memakai First Name `Budi`, Division `Finance`, Access `Fixed Asset`.
  - TC-GS-USER-115 Expected b mensyaratkan sel Employee ID `—`; TC tidak menyebut kolom Employee ID harus terlihat. Kolom itu tampil default (TC-GS-USER-1).
  - TC-GS-USER-125 Expected b "`Temporary until [tanggal besok]`" tidak menyebut format tanggal; spec memakai format tanggal General Settings client.
  - TC-GS-USER-138 langkah 2 menyebut checkbox `Stay on this form`, sedangkan PRD dan TC-GS-USER-139 menyebut `Stay on this form after submitting`; spec memakai label yang kedua.
  - TC-GS-USER-138 tidak menyebut Email, Last Name pembeda, dan field wajib lain untuk ketiga user; spec memakai nilai bersuffix di Prerequisites.
  - TC-GS-USER-138 Post Condition "3 user populasi tersedia untuk TC Search/Filter/Delete" tidak punya langkah observasi dan tidak diasersi. User spec ini dibersihkan di hook `after` dan tidak dipakai TC lain (S-06).
  - TC-GS-USER-109, 113, 115, 116, 125, 138: TC mengisi Emergency Phone (Pre-setup No. 24; Required nonaktif untuk TC ini) pada langkah 2 TC kecuali TC-GS-USER-113 yang menulis "Isi field wajib"; spec mengisi Emergency Phone pada semua Create dengan Country Code `🇮🇩 +62` dan Number `81234567890`.
