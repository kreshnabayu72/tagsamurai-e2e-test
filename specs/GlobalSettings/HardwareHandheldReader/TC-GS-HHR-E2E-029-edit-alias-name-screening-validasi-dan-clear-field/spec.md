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
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10, Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Spec memakai DD-01 (Serial Number `SN-HHR-00101`, Alias Name `—`) dan DD-02 (`Gudang Reader - 1`, Serial Number `SN-HHR-00102`, Alias Name `Reader Gudang 02`). Seed Reader A bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number. Alias Name tidak wajib unik (TC-GS-HHR-111), sehingga nilai alias uji ditulis literal sesuai TC.
- Cleanup: Seed Reader A dipulihkan ke kondisi awal Tabel Data Uji Dinamis oleh fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme pemulihan disediakan tim FE/BE (lihat Temuan untuk QA).
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
12. Verifikasi tidak ada pesan error inline pada input (status validasi pristine)
13. Klik `[✕]`
14. Verifikasi dialog `Unsaved Changes` muncul
15. Klik `[Leave]`

### TC-GS-HHR-462: Navigasi keyboard: fokus terkunci di dalam dialog dan Esc menutup

16. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
17. Tekan `Tab` berulang hingga fokus melewati seluruh elemen interaktif dialog
18. Verifikasi fokus hanya berpindah di antara `[✕]`, input `Alias Name`, `[Clear Field]`, dan `[Save]`, lalu kembali ke elemen pertama sesudah elemen terakhir
19. Verifikasi fokus tidak keluar ke tabel di belakang dialog
20. Tekan `Shift+Tab` dari elemen interaktif pertama
21. Verifikasi fokus berpindah ke elemen terakhir dialog (`[Save]`)
22. Tekan `Esc`
23. Verifikasi dialog tertutup
24. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-HHR-112: Emoji pada Alias Name diblok di input

25. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
26. Ketik emoji `😊` pada `Alias Name`
27. Verifikasi emoji tidak masuk ke field
28. Tempel emoji `😊` pada `Alias Name`
29. Verifikasi emoji tidak masuk ke field
30. Verifikasi tidak ada pesan error

### TC-GS-HHR-110: Alias Name 121 karakter menonaktifkan Save

31. Isi `Alias Name` dengan 121 karakter `A`
32. Verifikasi pesan inline `Max. 120 characters`
33. Verifikasi `[Save]` disabled
34. Arahkan kursor ke `[Save]`
35. Verifikasi alasan disabled ditampilkan lewat pesan inline, tidak ada tooltip
36. Klik `[Clear Field]`

### TC-GS-HHR-113: Emoji yang lolos filter FE ditolak server

37. Injeksi nilai `😊` langsung ke DOM field `Alias Name` (melewati filter keystroke FE)
38. Klik `[Save]`
39. Verifikasi respons server atas request edit berstatus 422
40. Verifikasi pesan inline `Alias name contains invalid characters`
41. Verifikasi dialog tetap terbuka
42. Verifikasi input `Alias Name` mempertahankan nilai `😊`
43. Klik `[✕]`
44. Verifikasi dialog `Unsaved Changes` muncul
45. Klik `[Leave]`
46. Verifikasi kolom `Alias Name` baris DD-01 tetap `—`

### TC-GS-HHR-109: Alias Name tepat 120 karakter valid

47. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
48. Isi `Alias Name` dengan 120 karakter `A`
49. Verifikasi tidak ada pesan error
50. Verifikasi `[Save]` enabled
51. Klik `[Save]`
52. Verifikasi kolom `Alias Name` baris DD-01 menampilkan 120 karakter `A`

### TC-GS-HHR-111: Alias yang sama dengan alias reader lain diperbolehkan

53. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
54. Ganti isi `Alias Name` dengan `Reader Gudang 02`
55. Klik `[Save]`
56. Verifikasi tidak ada pesan `already exists`
57. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Gudang 02`
58. Verifikasi kolom `Alias Name` baris DD-02 menampilkan `Reader Gudang 02`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 103 dan 114, 462, 112, 110, 113, 109, 111. Urutan menyimpang dari urutan TC sumber dan mengikuti kondisi form dan data: screening 103 memakai `[Clear Field]` sebagai langkah yang diuji TC-GS-HHR-114 pada form yang sama; validasi yang diblokir (112, 110, 113) berada sebelum Save yang berhasil (109, 111); TC-GS-HHR-113 mengasersi `Alias Name` DD-01 tetap `—`, sehingga harus mendahului TC-GS-HHR-109 yang mengubah alias DD-01.
- Jumlah pembukaan dialog Edit Alias Name: 5 (langkah 1, 16, 25, 47, 53); jumlah kejadian menutup: 5 (langkah 13 sampai 15, langkah 22, langkah 43 sampai 45, langkah 51, langkah 55).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 sampai 15 (menutup form dirty lewat `✕` lalu `[Leave]`, S-08; TC-GS-HHR-114 tidak menyebut cara menutup), langkah 36 (`[Clear Field]` membersihkan error inline 121 karakter sebelum TC-GS-HHR-113, S-09), langkah 34 (hover `[Save]` agar ketiadaan tooltip teramati), dan langkah 43 sampai 45 (menutup form dirty agar `Alias Name` baris dapat diasersi).
- Asersi absence pesan `already exists` (langkah 56) diletakkan segera sesudah pemicu `[Save]` (langkah 55) dan sebelum asersi hasil di tabel (bagian 8b butir 5 dan 11); asersi tabel yang menyusul menjadi anchor positif.
- Spec melewati sekitar 35 langkah (58 langkah). Seluruhnya satu topik dan satu kelas (dialog Edit Alias Name, akun dan dataset sama, tanpa harness eksternal; langkah 37 dan 39 hanya memakai injeksi DOM dan pembacaan respons sebagai pemicu dan pengamat). Tiap blok membuka dialog sendiri dan memulai dari field bersih, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan dialog.
- Alias Name pada TC-GS-HHR-109 dan 111 diubah pada DD-01 secara berurutan (120 karakter `A`, lalu `Reader Gudang 02`); nilai awal DD-01 untuk blok berikutnya tidak dipakai.
- Pembagian TC lintas spec: TC-GS-HHR-104 sampai 108, 120, 123, dan 124 ada di spec 030; TC-GS-HHR-115 sampai 119 ada di spec 031; TC-GS-HHR-121 dan 122 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-HHR-103 Expected b.i menyebut input terisi `Reader Gudang 02` bersamaan dengan placeholder `Enter alias name`; placeholder hanya teramati pada input kosong. Spec mengasersi placeholder sesudah `[Clear Field]` (langkah 9, S-14).
  - TC-GS-HHR-113 mensyaratkan injeksi nilai langsung ke DOM dan status 422; mekanisme injeksi dan pembacaan respons tidak didefinisikan di TC, PRD, atau LLD. Spec menulis kemampuannya di Prerequisites tanpa mengarang endpoint; status 422 diasersi dari respons jaringan browser (bukan request langsung ke server).
  - TC-GS-HHR-109 Expected b ("Alias Name tersimpan 120 karakter `A`") tidak menyebut cara membaca 120 karakter pada sel tabel yang dapat terpotong; spec mengasersi nilai sel kolom `Alias Name`.
  - TC-GS-HHR-114 Expected c ("Status validasi pristine") tidak punya penanda yang teramati; spec mengasersi tidak ada pesan error inline.
  - TC-GS-HHR-462 tidak menyebut elemen yang terfokus saat dialog dibuka; spec memulai `Tab` dan `Shift+Tab` sesuai langkah TC dan mengasersi siklus fokus.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.
