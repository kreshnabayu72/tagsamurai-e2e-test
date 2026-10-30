---
id: TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field
title: "Create Position: Screening Form, Aksesibilitas, Validasi Inline (Kosong, Spasi, 121 Karakter, Emoji), Clear Field, dan Hover Tombol"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-37
  - TC-GS-POS-38
  - TC-GS-POS-39
  - TC-GS-POS-40
  - TC-GS-POS-42
  - TC-GS-POS-43
  - TC-GS-POS-44
  - TC-GS-POS-45
  - TC-GS-POS-50
  - TC-GS-POS-284
coverage:
  web: automated
---

# Create Position: Screening Form, Aksesibilitas, Validasi Inline (Kosong, Spasi, 121 Karakter, Emoji), Clear Field, dan Hover Tombol

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`; langkah 1 langsung membuka popup Create.
- Data Pre-setup (tetap di environment, hanya dibaca, tidak diubah, tanpa suffix): Position 10 `IT Manager` sebagai nama yang sudah ada untuk memicu error duplikat pada TC-GS-POS-50.
- Data Dinamis: tidak ada record yang dibuat. Semua Submit pada spec ini diblokir validasi. Nilai input uji (satu karakter valid `A` pada langkah 35 dan 42, 3 spasi, nama 121 karakter, 119 karakter + 2 spasi, `Sales Lead` + 🚀, `Sales 🚀 Lead`) hanya diketik atau di-paste dan tidak pernah tersimpan; `A` hanya pembersih error antar TC dan tidak disubmit. Nilai 121 karakter dan 119 karakter + 2 spasi memakai teks Data Uji TC-GS-POS-42 dan TC-GS-POS-43 apa adanya; fixture baru `Fixture.position.createValidation011`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): bila Submit nama 121 karakter pada langkah 53 ternyata menghasilkan record, hapus lewat API Position bernama nilai itu.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: pembacaan atribut ARIA (`aria-required`, `aria-describedby`) pada input; penekanan tombol Tab berulang dan pembacaan elemen yang sedang fokus; pengisian clipboard lalu paste (Ctrl+V) berisi emoji; pengetikan emoji lewat keyboard; hover pada tombol dan pembacaan state visual (background, warna teks, border).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-POS-37: Screening Popup Create Position, 3 zona

1. Klik `[+ Position]`
2. Verifikasi Header menampilkan Title "Create Position"
3. Verifikasi Header menampilkan icon close `[✕]` di kanan atas
4. Verifikasi Body menampilkan label "Position Name *"
5. Verifikasi input Position Name kosong dengan placeholder "Enter position name"
6. Verifikasi kursor otomatis fokus di input Position Name
7. Verifikasi Footer menampilkan checkbox "Stay on this form after submitting" dalam keadaan unchecked
8. Verifikasi checkbox "Stay on this form after submitting" rata kanan
9. Verifikasi checkbox "Stay on this form after submitting" berada di atas baris tombol
10. Verifikasi tombol di Footer rata kanan
11. Verifikasi urutan tombol di Footer `[Clear Field]` lalu `[Submit]`
12. Verifikasi `[Clear Field]` bergaya text (primary)
13. Verifikasi `[Submit]` bergaya filled (success)
14. Verifikasi tidak ada tombol `[Cancel]` di Footer

### TC-GS-POS-284: Feedback hover tombol Submit dan Clear Field

15. Hover `[Submit]`
16. Verifikasi `[Submit]` menampilkan background success hover
17. Hover `[Clear Field]`
18. Verifikasi `[Clear Field]` menampilkan state hover text primary

### TC-GS-POS-38: Aksesibilitas Popup Create Position, aria-required, aria-describedby, dan focus trap

19. Verifikasi input Position Name memiliki `aria-required="true"`
20. Klik `[Submit]` dengan input kosong
21. Verifikasi error "Position Name must not be empty" tampil
22. Verifikasi input Position Name memiliki `aria-describedby` yang menunjuk elemen pesan error
23. Klik input Position Name
24. Tekan Tab
25. Verifikasi fokus berada di checkbox "Stay on this form after submitting"
26. Tekan Tab
27. Verifikasi fokus berada di `[Clear Field]`
28. Tekan Tab
29. Verifikasi fokus berada di `[Submit]`
30. Tekan Tab
31. Verifikasi fokus berada di `[✕]`
32. Tekan Tab
33. Verifikasi fokus kembali ke input Position Name
34. Verifikasi fokus tidak keluar ke halaman di belakang popup

### TC-GS-POS-39: Position Name kosong saat Submit

35. Ketik satu karakter valid `A` pada Position Name
36. Kosongkan Position Name (pilih seluruh teks lalu hapus)
37. Klik `[Submit]` dengan Position Name kosong
38. Verifikasi error inline "Position Name must not be empty" tampil di bawah field
39. Verifikasi border field ber-severity danger
40. Verifikasi popup tetap terbuka
41. Verifikasi tidak ada toast

### TC-GS-POS-40: Position Name hanya berisi spasi saat Submit

42. Ketik satu karakter valid `A` pada Position Name
43. Kosongkan Position Name (pilih seluruh teks lalu hapus)
44. Ketik 3 spasi pada Position Name
45. Klik `[Submit]`
46. Verifikasi error inline "Position Name must not be empty" tampil (spasi dianggap kosong setelah trim)
47. Verifikasi popup tetap terbuka
48. Verifikasi tidak ada toast

### TC-GS-POS-42: Position Name 121 karakter memunculkan error langsung

49. Kosongkan Position Name (pilih seluruh teks lalu hapus)
50. Ketik nama 121 karakter pada Position Name tanpa memindahkan fokus
51. Verifikasi error inline "Max. 120 characters" tampil langsung saat karakter ke-121 diketik, sebelum Submit
52. Verifikasi fokus masih di Position Name (error muncul tanpa pindah fokus)
53. Klik `[Submit]`
54. Verifikasi popup tetap terbuka
55. Verifikasi tidak ada toast sukses

### TC-GS-POS-43: Batas 120 karakter dihitung sebelum trim

56. Kosongkan Position Name (pilih seluruh teks lalu hapus)
57. Ketik 119 karakter lalu tambahkan 2 spasi di akhir (total 121 karakter mentah)
58. Verifikasi error inline "Max. 120 characters" tampil langsung karena 121 karakter dihitung sebelum trim

### TC-GS-POS-44: Mengetik emoji pada Position Name

59. Kosongkan Position Name (pilih seluruh teks lalu hapus)
60. Ketik `Sales Lead`
61. Ketik emoji 🚀
62. Verifikasi emoji tidak masuk ke nilai field
63. Verifikasi nilai field tetap `Sales Lead`
64. Verifikasi tidak ada pesan error inline "Position Name contains invalid characters"

### TC-GS-POS-45: Paste teks berisi emoji pada Position Name

65. Kosongkan Position Name (pilih seluruh teks lalu hapus)
66. Paste `Sales 🚀 Lead` ke Position Name
67. Verifikasi emoji tidak masuk ke nilai field
68. Verifikasi sisa teks tanpa emoji (`Sales` dan `Lead`) tetap masuk ke nilai field
69. Verifikasi tidak ada pesan error inline "Position Name contains invalid characters"

### TC-GS-POS-50: Clear Field mengosongkan form tanpa menutup

70. Kosongkan Position Name (pilih seluruh teks lalu hapus)
71. Centang `Stay on this form after submitting`
72. Ketik `IT Manager` pada Position Name, tunggu error duplikat
73. Verifikasi error inline "Position Name already exists" tampil
74. Verifikasi border danger tampil
75. Klik `[Clear Field]`
76. Verifikasi Position Name kosong
77. Verifikasi error inline hilang
78. Verifikasi border danger hilang
79. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
80. Verifikasi popup tetap terbuka
81. Verifikasi fokus kembali ke Position Name
82. Verifikasi dialog Unsaved Changes tidak muncul
83. Klik `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 37, 284, 38, 39, 40, 42, 43, 44, 45, 50. Hover (TC-GS-POS-284) dan fokus awal (TC-GS-POS-37 langkah 6) diasersi sebelum langkah yang mengubah state-nya (hover dan fokus berpindah oleh klik berikutnya). TC-GS-POS-284 dipindah ke depan TC-GS-POS-38 dari posisi terakhir di TC sumber. TC-GS-POS-50 ditaruh paling akhir karena mengaktifkan Stay dan mengosongkan form lewat `[Clear Field]`. Seluruh spec memakai satu pembukaan form (langkah 1) dengan field dikosongkan di antara kasus, dan satu kejadian menutup form (langkah 83).
- TC-GS-POS-38 langkah 3 dan TC-GS-POS-39 langkah 3 sama-sama mengklik `[Submit]` pada form kosong; klik dilakukan dua kali (langkah 20 dan 37) agar tiap blok TC memiliki aksi pemicunya sendiri. Error dari langkah 21 dibersihkan lebih dulu pada langkah 35 sampai 36 (ketik satu karakter valid lalu kosongkan) supaya langkah 38 sampai 39 tidak lulus karena error lama; error dari blok TC-GS-POS-39 dibersihkan dengan cara yang sama pada langkah 42 sampai 43 sebelum TC-GS-POS-40.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 23 (memfokuskan input sebelum Tab pertama), langkah 35 sampai 36 dan 42 sampai 43 (membersihkan error inline antar TC), langkah 49, 56, 59, 65, dan 70 (mengosongkan Position Name tanpa `[Clear Field]` supaya `[Clear Field]` hanya diuji di TC-GS-POS-50), langkah 71 (mengatur Stay untuk TC-GS-POS-50), dan langkah 83 (menutup popup; form kosong sehingga tidak ada dialog `Unsaved Changes`, sama seperti Expected e TC-GS-POS-50).
- Langkah 73 dan 74 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-50: error duplikat harus tampil dulu agar Expected b ("error dan border danger hilang") bermakna; Step 3 TC-GS-POS-50 menyebut "hingga error duplikat tampil".
- Langkah 21 pada TC-GS-POS-38 mengasersi teks error yang sama dengan Expected b TC-GS-POS-38 sebagai prasyarat `aria-describedby`.
- Pembagian TC lintas spec: TC-GS-POS-46 dan 84 (emoji lolos filter FE ditolak server) ada di spec 049; TC-GS-POS-41 ada di spec 014; TC-GS-POS-47, 48, dan 49 ada di spec 012; TC-GS-POS-55 sampai 64 ada di spec 013.
- Spec melewati sekitar 35 langkah (83 langkah). Seluruhnya satu kelas (tampilan dan validasi form Create), satu akun, satu pembukaan form, tanpa membuat atau mengubah data; tiap blok kasus mengosongkan field lebih dulu dan tetap bermakna bila blok lain gagal (kegagalan keras hanya bila popup tidak terbuka).
- Temuan untuk QA:
  - TC-GS-POS-50 tidak mencantumkan "record `IT Manager` sudah ada" di Precondition, padahal Step 3 membutuhkannya untuk memunculkan error duplikat; spec memakai Pre-setup 10 `IT Manager` (hanya dibaca).
  - Post Condition "Tidak ada record baru" pada TC-GS-POS-39, 40, 42, dan 43 tidak punya langkah observasi di TC sehingga tidak diasersi. Expected TC-GS-POS-42 b hanya menyebut popup tetap terbuka dan tidak ada toast sukses.
  - TC-GS-POS-45 menyebut "sisa teks tanpa emoji tetap masuk" tanpa menyebut nilai akhir persis (`Sales  Lead` dengan dua spasi atau `Sales Lead`); spec hanya mengasersi bahwa `Sales` dan `Lead` ada dan emoji tidak ada.
  - TC-GS-POS-284 tidak menyebut warna atau token style persis untuk "background success hover" dan "text primary hover"; asersi mengikuti kata-kata TC.
  - TC-GS-POS-38 langkah 4 tidak menyebut elemen yang sedang fokus saat Tab pertama ditekan; spec memfokuskan input Position Name lebih dulu (langkah 23).
  - Perilaku error "Position Name must not be empty" saat field dikosongkan lagi sesudah mengetik satu karakter valid (langkah 35 sampai 36 dan 42 sampai 43) belum dikonfirmasi FE: bila error muncul kembali segera saat dikosongkan, langkah pembersih tidak menghilangkan error dan TC-GS-POS-39 serta TC-GS-POS-40 perlu form baru. Menunggu konfirmasi FE.
  - TC-GS-POS-43 tidak menyebut Submit sehingga hanya error inline yang diasersi.
