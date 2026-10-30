---
id: TC-GS-USER-E2E-020-create-screening-popup-opsi-access-position-division-dan-aksesibilitas
title: "Create User: Screening Popup, Opsi Access, Opsi Position dan Division dari Master Data, dan Fokus Terkunci"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-88
  - TC-GS-USER-89
  - TC-GS-USER-90
  - TC-GS-USER-148
coverage:
  web: automated
---

# Create User: Screening Popup, Opsi Access, Opsi Position dan Division dari Master Data, dan Fokus Terkunci

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data):
  - Client PT Maju Bersama, plan Growth, subscription Fixed Asset dan Supply Asset aktif (No. 26).
  - Custom Field aktif `Blood Type` (Dropdown), `Skills` (Multi-Dropdown), `Emergency Phone` (Phone, Required) (No. 24).
  - Master Data Position: `Finance Manager`, `HR Business Partner`, `Staff`, `Supervisor`, `Internal Auditor` (No. 22). `Internal Auditor` aktif dan belum dipakai user mana pun; kondisi "belum dipakai" disediakan tim FE pada data Pre-setup (Tabel Pre-setup tidak menyebutnya).
  - Master Data Division: `Finance`, `General Affairs`, `Logistics`, `Legal` (No. 23).
- Data Dinamis: tidak ada; spec tidak membuat data dan tidak menekan `[Submit]`.
- State global yang diubah (TC-GS-USER-89): subscription Client uji diubah menjadi hanya Fixed Asset (Supply Asset tidak disubscribe). Mekanisme mengubah dan memulihkan subscription tidak disebut di TC, PRD, atau LLD, sehingga disediakan tim FE/BE. Hook `before` mencatat subscription awal; hook `after` memulihkannya ke Fixed Asset dan Supply Asset walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca daftar Position aktif dan daftar Division aktif Master Data dari backend sebagai pembanding isi dropdown (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD); menekan tombol Tab di dalam Popup; mengamati elemen yang sedang fokus.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-88: Screening Popup Create User

2. Klik `[+ User]` di Table Tools
3. Verifikasi Header Popup: Title `Create User`
4. Verifikasi Header Popup: icon `✕` tampil
5. Verifikasi Body: Photo upload berada di baris pertama
6. Verifikasi Body: Photo upload center-aligned
7. Verifikasi Body: avatar Photo upload kosong
8. Verifikasi Body grid 2 kolom baris pertama: `First Name *` (placeholder `Enter first name`) di kolom kiri dan `Last Name *` (placeholder `Enter last name`) di kolom kanan
9. Verifikasi Body grid 2 kolom baris kedua: `Position` (placeholder `Select position`) di kolom kiri dan `Division *` (placeholder `Select division`) di kolom kanan
10. Verifikasi Body grid 2 kolom baris ketiga: `Employee ID` (placeholder `Enter employee ID`) di kolom kiri dan `Email *` (placeholder `Enter email address`) di kolom kanan
11. Verifikasi Body: `Employee ID` tanpa helper text
12. Verifikasi Body: `Access *` membentang 2 kolom
13. Verifikasi Body: checkbox group `Access *` berisi `Fixed Asset` | `Global Settings` | `Supply Asset`
14. Verifikasi Body: tidak ada checkbox Access yang tercentang
15. Verifikasi Body: `User TAG` menampilkan badge `Unverified` dengan varian warning
16. Verifikasi Body: `User TAG` menampilkan tombol `Scan TAG`
17. Verifikasi Body: checkbox `Set as Temporary User` tidak tercentang
18. Verifikasi Body: field `Temporary Until` belum tampil
19. Verifikasi Body: divider full-width tampil di bawah bagian `Set as Temporary User`
20. Verifikasi Body: di bawah divider tampil Custom Field `Blood Type` | `Skills` | `Emergency Phone`
21. Verifikasi Footer: checkbox `Stay on this form after submitting` tidak tercentang
22. Verifikasi Footer: urutan elemen checkbox `Stay on this form after submitting`, `[Clear Field]`, lalu `[Submit]`

### TC-GS-USER-90: Opsi Position dan Division diambil dari Master Data aktif

23. Klik dropdown Position
24. Verifikasi dropdown Position memuat `Internal Auditor`
25. Verifikasi dropdown Position memuat `Finance Manager`, `HR Business Partner`, `Staff`, dan `Supervisor`
26. Verifikasi isi dropdown Position sama dengan seluruh Position aktif Master Data yang dibaca dari backend
27. Tutup dropdown Position dengan mengklik Title Popup `Create User`
28. Klik dropdown Division
29. Verifikasi dropdown Division memuat `Finance`, `General Affairs`, `Logistics`, dan `Legal`
30. Verifikasi isi dropdown Division sama dengan seluruh Division aktif Master Data yang dibaca dari backend
31. Tutup dropdown Division dengan mengklik Title Popup `Create User`

### TC-GS-USER-148: Accessibility Popup Create User, fokus terkunci

32. Tekan Tab berulang sebanyak jumlah elemen yang dapat difokus di Popup ditambah satu
33. Verifikasi fokus berputar kembali ke elemen pertama yang dapat difokus di Popup sesudah elemen terakhir
34. Verifikasi fokus tidak pernah keluar ke elemen halaman di belakang Popup pada setiap penekanan Tab
35. Klik `✕` di header Popup

### TC-GS-USER-89: Opsi Access menyembunyikan produk yang tidak disubscribe Client

36. Ubah subscription Client uji menjadi hanya Fixed Asset (Supply Asset tidak disubscribe)
37. Muat ulang halaman User List
38. Klik `[+ User]` di Table Tools
39. Verifikasi opsi Access `Fixed Asset` | `Global Settings` tampil
40. Verifikasi `Supply Asset` tidak dirender di Access (Hidden, bukan checkbox disabled)
41. Klik `✕` di header Popup

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: TC-GS-USER-88, 90, 148, lalu 89. TC-GS-USER-89 ditaruh terakhir karena mengubah subscription Client (state global) menjadi tanpa Supply Asset, sedangkan TC-GS-USER-88 mensyaratkan Fixed Asset dan Supply Asset aktif.
- TC-GS-USER-88, 90, dan 148 berbagi satu pembukaan Popup (prinsip 6 dan 8 bagian 3 konvensi). Fokus awal TC-GS-USER-148 adalah fokus sesudah dropdown ditutup pada langkah sebelumnya; asersi putaran fokus tidak bergantung pada elemen awal.
- Spec melewati sekitar 35 langkah (41 langkah) karena seluruh blok berada di satu kelas harness (screening fungsional, tanpa submit), memakai satu layar yang sama (Popup Create User), dan tiap blok berdiri sendiri; Verifikasi TC-GS-USER-88 dipecah per klausa (S-01) sehingga jumlah langkahnya besar.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup dropdown dengan mengklik Title Popup; `✕` di header Popup (form tidak dirty, tidak ada dialog); mengubah subscription Client dan memuat ulang halaman sebelum TC-GS-USER-89.
- Verifikasi isi dropdown sama dengan daftar Master Data dari backend memakai kemampuan baca yang disediakan tim FE/BE; Verifikasi `Supply Asset` tidak dirender didahului Verifikasi bahwa opsi `Fixed Asset` dan `Global Settings` pada checkbox group yang sama sudah tampil (8b butir 2).
- Temuan untuk QA:
  - TC-GS-USER-89 mensyaratkan Client hanya subscribe Fixed Asset, sedangkan TC-GS-USER-88 mensyaratkan Fixed Asset dan Supply Asset; TC tidak menyebut Client mana atau cara mengubah subscription. Disediakan tim FE/BE.
  - TC-GS-USER-90 mensyaratkan Position `Internal Auditor` belum dipakai user mana pun; Tabel Pre-setup No. 22 tidak menyebut kondisi ini. Spec tidak mengasersinya (precondition), disediakan tim FE.
  - TC-GS-USER-90 menyebut "seluruh Position aktif lain" dan "seluruh Division aktif Master Data" tanpa daftar; spec membandingkan dengan daftar aktif dari backend.
  - TC-GS-USER-148 tidak menyebut jumlah penekanan Tab atau elemen awal; spec memakai satu siklus penuh ditambah satu penekanan.
  - TC-GS-USER-88 tidak menyebut tanda wajib (`*`) pada Custom Field `Emergency Phone` (Required); spec mengikuti teks TC `Emergency Phone` tanpa tanda.
