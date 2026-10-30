---
id: TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field
title: "Edit Alias Name: Screening Dialog, Clear Field, Navigasi Keyboard, Emoji Diblok dan Ditolak Server, Batas 120 dan 121 Karakter, Alias Sama Diperbolehkan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-103
  - TC-GS-HHR-109
  - TC-GS-HHR-110
  - TC-GS-HHR-111
  - TC-GS-HHR-112
  - TC-GS-HHR-113
  - TC-GS-HHR-114
  - TC-GS-HHR-462
coverage:
  web: automated
---

# Edit Alias Name: Screening Dialog, Clear Field, Navigasi Keyboard, Emoji Diblok dan Ditolak Server, Batas 120 dan 121 Karakter, Alias Sama Diperbolehkan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah alias reader pada Seed Reader A (dipulihkan, lihat Cleanup), sehingga tidak berjalan bersamaan dengan spec lain pada Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A (DD-01 sampai DD-10, Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Spec memakai DD-01 (Serial Number `SN-HHR-00101`, Alias Name `—`) dan DD-02 (`Gudang Reader - 1`, Serial Number `SN-HHR-00102`, Alias Name `Reader Gudang 02`). Seed Reader A bernama literal tanpa suffix (pengecualian S-12 Population Seed Reader A HHR) karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number. Alias Name tidak wajib unik (TC-GS-HHR-111), sehingga nilai alias uji ditulis literal sesuai TC.
- Cleanup: Seed Reader A dipulihkan ke kondisi awal Tabel Data Uji Dinamis oleh fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`). Pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: input keyboard (`Tab`, `Shift+Tab`, `Esc`); menempel teks dari clipboard; menyetel nilai field langsung ke DOM dengan event input sehingga form menerima nilai (melewati filter keystroke FE); membaca respons jaringan browser atas request edit (status 422); klik pada area backdrop.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite) dan alias Seed Reader A (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-103 dan TC-GS-HHR-114: Screening Dialog Edit Alias Name, lalu Clear Field

1. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
2. Verifikasi judul Header dialog `Edit Alias Name`
3. Verifikasi ikon `[✕]` tampil pada Header
4. Verifikasi input teks `Alias Name` terisi nilai saat ini `Reader Gudang 02`
5. Verifikasi helper text `Max. 120 characters`
6. Verifikasi Footer berisi `[Clear Field]` dan `[Save]` tanpa `[Cancel]`
7. Klik `[Clear Field]`
8. Verifikasi input `Alias Name` kosong (bukan kembali ke nilai tersimpan)
9. Verifikasi placeholder `Enter alias name` pada input kosong
10. Verifikasi dialog tetap terbuka
11. Verifikasi tidak ada dialog konfirmasi
12. Verifikasi input `Alias Name` tanpa border merah
13. Verifikasi tidak ada pesan error inline pada input (status validasi pristine)
14. Klik `[✕]` pada header dialog
15. Verifikasi dialog `Unsaved Changes` muncul (nilai kosong berbeda dari nilai tersimpan `Reader Gudang 02`)
16. Klik `[Leave]` pada dialog `Unsaved Changes`
17. Verifikasi dialog Edit Alias Name tertutup
18. Verifikasi kolom `Alias Name` baris DD-02 tetap `Reader Gudang 02`

### TC-GS-HHR-462: Navigasi keyboard: fokus terkunci di dalam dialog dan Esc menutup

19. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
20. Tekan `Tab` berulang hingga fokus melewati seluruh elemen interaktif dialog
21. Verifikasi fokus hanya berpindah di antara `[✕]`, input `Alias Name`, `[Clear Field]`, dan `[Save]`, lalu kembali ke elemen pertama sesudah elemen terakhir
22. Verifikasi fokus tidak keluar ke tabel di belakang dialog
23. Tekan `Shift+Tab` dari elemen interaktif pertama
24. Verifikasi fokus berpindah ke elemen terakhir dialog (`[Save]`)
25. Tekan `Esc`
26. Verifikasi dialog tertutup
27. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-HHR-112: Emoji pada Alias Name diblok di input

28. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
29. Ketik emoji `😊` pada `Alias Name`
30. Verifikasi emoji tidak masuk ke field
31. Tempel emoji `😊` pada `Alias Name`
32. Verifikasi emoji tidak masuk ke field
33. Verifikasi tidak ada pesan error

### TC-GS-HHR-110: Alias Name 121 karakter menonaktifkan Save

34. Isi `Alias Name` dengan 121 karakter `A`
35. Verifikasi pesan inline `Max. 120 characters`
36. Verifikasi `[Save]` disabled
37. Arahkan kursor ke `[Save]`
38. Verifikasi alasan disabled ditampilkan lewat pesan inline, tidak ada tooltip
39. Klik `[Clear Field]`

### TC-GS-HHR-113: Emoji yang lolos filter FE ditolak server

40. Injeksi nilai `😊` langsung ke DOM field `Alias Name` (melewati filter keystroke FE)
41. Klik `[Save]`
42. Verifikasi respons server atas request edit berstatus 422
43. Verifikasi pesan inline `Alias name contains invalid characters`
44. Verifikasi dialog tetap terbuka
45. Verifikasi input `Alias Name` mempertahankan nilai `😊`
46. Klik `[✕]`
47. Verifikasi dialog `Unsaved Changes` muncul
48. Klik `[Leave]`
49. Verifikasi kolom `Alias Name` baris DD-01 tetap `—`

### TC-GS-HHR-109: Alias Name tepat 120 karakter valid

50. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
51. Isi `Alias Name` dengan 120 karakter `A`
52. Verifikasi tidak ada pesan error
53. Verifikasi `[Save]` enabled
54. Klik `[Save]`
55. Verifikasi kolom `Alias Name` baris DD-01 menampilkan 120 karakter `A`

### TC-GS-HHR-111: Alias yang sama dengan alias reader lain diperbolehkan

56. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
57. Ganti isi `Alias Name` dengan `Reader Gudang 02`
58. Klik `[Save]`
59. Verifikasi tidak ada pesan `already exists`
60. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Gudang 02`
61. Verifikasi kolom `Alias Name` baris DD-02 menampilkan `Reader Gudang 02`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 103 dan 114, 462, 112, 110, 113, 109, 111. Urutan menyimpang dari urutan TC sumber dan mengikuti kondisi form dan data: screening 103 memakai `[Clear Field]` sebagai langkah yang diuji TC-GS-HHR-114 pada form yang sama; validasi yang diblokir (112, 110, 113) berada sebelum Save yang berhasil (109, 111); TC-GS-HHR-113 mengasersi `Alias Name` DD-01 tetap `—`, sehingga harus mendahului TC-GS-HHR-109 yang mengubah alias DD-01.
- Jumlah pembukaan dialog Edit Alias Name: 5 (langkah 1, 19, 28, 50, 56); jumlah kejadian menutup: 5 (langkah 14 sampai 16, langkah 25, langkah 46 sampai 48, langkah 54, langkah 58).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 39 (`[Clear Field]` membersihkan error inline 121 karakter sebelum TC-GS-HHR-113, S-09), langkah 37 (hover `[Save]` agar ketiadaan tooltip teramati), dan langkah 46 sampai 48 (menutup form dirty agar `Alias Name` baris dapat diasersi).
- Asersi absence pesan `already exists` (langkah 59) diletakkan segera sesudah pemicu `[Save]` (langkah 58) dan sebelum asersi hasil di tabel (bagian 8b butir 5 dan 11); asersi tabel yang menyusul menjadi anchor positif.
- Spec melewati sekitar 35 langkah (61 langkah). Seluruhnya satu topik dan satu kelas (dialog Edit Alias Name, akun dan dataset sama, tanpa harness eksternal; langkah 40 dan 42 hanya memakai injeksi DOM dan pembacaan respons sebagai pemicu dan pengamat). Tiap blok membuka dialog sendiri dan memulai dari field bersih, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan dialog.
- Alias Name pada TC-GS-HHR-109 dan 111 diubah pada DD-01 secara berurutan (120 karakter `A`, lalu `Reader Gudang 02`); nilai awal DD-01 untuk blok berikutnya tidak dipakai.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Spec 029, 030, dan 031 menguji dialog Edit Alias Name pada dataset Seed Reader A yang sama dan sengaja dipisah: gabungannya 163 langkah (61, 74, dan 28), jauh di atas sekitar 35 langkah, dan tiap spec membuka dialog sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Pembagian TC lintas spec: TC-GS-HHR-104 sampai 108, 120, 123, dan 124 ada di spec 030; TC-GS-HHR-115 sampai 119 ada di spec 031; TC-GS-HHR-121 dan 122 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-HHR-103 Expected b.i menyebut input terisi `Reader Gudang 02` bersamaan dengan placeholder `Enter alias name`; placeholder hanya teramati pada input kosong. Spec mengasersi placeholder sesudah `[Clear Field]` (langkah 9, S-14).
  - TC-GS-HHR-113 mensyaratkan injeksi nilai langsung ke DOM dan status 422; mekanisme injeksi dan pembacaan respons tidak didefinisikan di TC, PRD, atau LLD. Spec menulis kemampuannya di Prerequisites tanpa mengarang endpoint; status 422 diasersi dari respons jaringan browser (bukan request langsung ke server).
  - TC-GS-HHR-109 Expected b ("Alias Name tersimpan 120 karakter `A`") tidak menyebut cara membaca 120 karakter pada sel tabel yang dapat terpotong; spec mengasersi nilai sel kolom `Alias Name`.
  - TC-GS-HHR-462 tidak menyebut elemen yang terfokus saat dialog dibuka; spec memulai `Tab` dan `Shift+Tab` sesuai langkah TC dan mengasersi siklus fokus.
  - Tidak ada Post Condition pada TC sumber spec ini.
