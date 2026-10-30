---
id: TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again
title: "Resilience Tulis: Create dan Edit Gagal 5xx, Timeout lalu Try Again, dan Cek Keunikan Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-49
  - TC-GS-UOM-67
  - TC-GS-UOM-68
  - TC-GS-UOM-89
  - TC-GS-UOM-90
  - TC-GS-UOM-343
  - TC-GS-UOM-352
coverage:
  web: automated
---

# Resilience Tulis: Create dan Edit Gagal 5xx, Timeout lalu Try Again, dan Cek Keunikan Gagal

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi; kelas fault injection, prinsip 13b). Kegagalan dipicu dengan `Spectra.intercept()` pada request browser; bukan `Mode: mock` karena Expected Result mengasersi data yang tersimpan di backend (League tersimpan satu kali, Symbol baris Tray).
- Hook suite (login akun default Total Control Client A, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`. Password dari `Spectra.env.GS_TC_PASSWORD`; tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run dan nomor spec, S-12):
  - `Kelvin {runId}-023` / `K` (D-05): dibuat sukses lewat UI di TC-GS-UOM-49.
  - `Mile {runId}-023` / `mi`: input Create yang dipaksa gagal (tidak membuat data).
  - `League {runId}-023` / `lea`: dibuat sukses lewat Try Again di TC-GS-UOM-343.
  - `Fail Edit {runId}-023` / `fe`: unit bebas relasi di-seed lewat API di hook `before`, target Edit yang dipaksa gagal (menggantikan Liter di TC-GS-UOM-89 dan 90 agar baris Pre-setup bersama tidak berubah, S-06).
  - `Tray {runId}-023` / `tr` (D-35): unit bebas relasi di-seed lewat API di hook `before`, target Edit TC-GS-UOM-352.
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request ke endpoint Measurement dan dilepas segera setelah dipakai (S-09):
  - respons cek keunikan Unit Name dipaksa timeout (TC-GS-UOM-49);
  - respons Create dipaksa HTTP 500 (TC-GS-UOM-67);
  - respons Create dipaksa timeout: request ditahan melewati batas klien dan tidak diteruskan ke server, sehingga retry setelah [Try Again] membuat unit satu kali (TC-GS-UOM-68, 343);
  - respons Edit dipaksa HTTP 500 (TC-GS-UOM-89);
  - respons Edit dipaksa timeout (TC-GS-UOM-90 dan 352; pada TC-GS-UOM-352 timeout hanya sekali).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): lepaskan semua intercept; hapus lewat API `Kelvin {runId}-023`, `Mile {runId}-023`, `League {runId}-023`, `Fail Edit {runId}-023`, dan `Tray {runId}-023` bila masih ada.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa 500 dan timeout per endpoint (cek keunikan, Create, Edit), termasuk timeout satu kali; klik pada toast `[Try Again]`; pembacaan toast persisten.
- State global: tidak ada yang diubah selain intercept (dilepas di langkah 9, 22, 32, 47, 52, dan 64). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UOM-49: Cek keunikan real-time gagal tidak memblokir Submit

1. Pasang intercept: respons cek keunikan Unit Name timeout
2. Klik [+ Unit]
3. Ketik Unit Name `Kelvin {runId}-023` dan Symbol `K`
4. Tunggu cek keunikan selesai gagal
5. Verifikasi tidak ada error inline saat cek gagal
6. Verifikasi tombol [Submit] tetap aktif
7. Klik [Submit]
8. Verifikasi toast sukses: "Success, unit has been created."
9. Lepas intercept cek keunikan

### TC-GS-UOM-67: Create gagal 5xx mempertahankan form dan input

10. Pasang intercept: respons Create HTTP 500
11. Klik [+ Unit]
12. Isi Unit Name `Mile {runId}-023` dan Symbol `mi`
13. Klik [Submit]
14. Verifikasi toast error "Error, failed to create unit." tampil
15. Verifikasi toast error tampil di kanan bawah
16. Amati toast error selama 10 detik
17. Verifikasi toast error tetap tampil sampai di-dismiss
18. Verifikasi form tetap terbuka
19. Verifikasi input `Mile {runId}-023` dan `mi` dipertahankan
20. Verifikasi tombol [Submit] enabled kembali untuk retry
21. Tutup toast error secara manual

### TC-GS-UOM-68: Create timeout menampilkan toast koneksi dengan Try Again

22. Lepas intercept 500, lalu pasang intercept: respons Create timeout
23. Klik [Submit] pada form yang masih berisi `Mile {runId}-023` dan `mi`
24. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
25. Verifikasi form tetap terbuka
26. Verifikasi input `Mile {runId}-023` dan `mi` dipertahankan
27. Tutup toast koneksi

### TC-GS-UOM-343: Try Again pada toast koneksi mengulang Create dengan input yang sama

28. Ganti isi Unit Name dengan `League {runId}-023` dan Symbol dengan `lea`
29. Klik [Submit]
30. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
31. Verifikasi form tetap terbuka
32. Pulihkan respons normal (lepas intercept Create timeout)
33. Klik [Try Again] pada toast
34. Verifikasi Create diulang dengan `League {runId}-023` dan `lea`: toast sukses "Success, unit has been created."
35. Ketik Search `League {runId}-023`, tekan Enter
36. Verifikasi tepat satu baris `League {runId}-023` (hanya satu League tersimpan)
37. Klik `(←)` pada kotak Search

### TC-GS-UOM-89: Edit gagal 5xx mempertahankan form

38. Pasang intercept: respons Edit HTTP 500
39. Ketik Search `Fail Edit {runId}-023`, tekan Enter
40. Klik `⋯` baris `Fail Edit {runId}-023` > Edit
41. Ubah Symbol menjadi `lt`
42. Klik [Save]
43. Verifikasi toast error "Error, failed to update unit." tampil
44. Verifikasi form tetap terbuka dengan Symbol `lt`
45. Verifikasi tombol [Save] enabled kembali sehingga retry manual tersedia
46. Tutup toast error secara manual

### TC-GS-UOM-90: Edit timeout menampilkan toast koneksi

47. Lepas intercept 500, lalu pasang intercept: respons Edit timeout
48. Klik [Save] pada form yang masih berisi Symbol `lt`
49. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
50. Verifikasi form tetap terbuka
51. Tutup toast koneksi
52. Lepas intercept Edit timeout
53. Klik `[✕]` untuk menutup form yang masih dirty
54. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
55. Klik [Leave]
56. Verifikasi Symbol baris `Fail Edit {runId}-023` tetap `fe` (data tidak berubah)

### TC-GS-UOM-352: Try Again pada toast koneksi mengulang Edit dengan input yang sama

57. Pasang intercept: respons Edit timeout sekali
58. Ganti isi kotak search dengan `Tray {runId}-023`, tekan Enter
59. Klik `⋯` baris `Tray {runId}-023` > Edit
60. Ubah Symbol menjadi `try`
61. Klik [Save]
62. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
63. Verifikasi form tetap terbuka dengan Symbol `try`
64. Pulihkan respons normal (lepas intercept Edit)
65. Klik [Try Again] pada toast
66. Verifikasi Edit diulang dengan Symbol `try`: toast sukses "Success, unit has been updated."
67. Verifikasi modal tertutup
68. Verifikasi baris `Tray {runId}-023` menampilkan Symbol `try`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas fault injection (prinsip 13b) dengan intercept parsial di atas backend nyata.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan sumber dengan Create dahulu (49, 67, 68, 343), lalu Edit (89, 90, 352). TC-GS-UOM-67, 68, dan 343 memakai satu form Create yang dibuka pada langkah 11 dan dipakai ulang (hemat buka form, prinsip 6 dan 8): form tidak ditutup di antara TC, input diganti ke `League {runId}-023` (langkah 28) sesuai Data Uji TC-GS-UOM-343 dan form baru menutup sendiri sesudah Create sukses (langkah 34, Stay tidak dicentang). TC-GS-UOM-89 dan 90 memakai satu form Edit (langkah 40) yang ditutup di langkah 53 sampai 55; TC-GS-UOM-352 membuka form Edit baru.
- Langkah Uji TC-GS-UOM-343 "Klik [+ Unit], isi ..." tidak diulang karena form dari TC-GS-UOM-67 dan 68 masih terbuka; Langkah Uji TC-GS-UOM-90 "Edit ..., Symbol `lt`" dan TC-GS-UOM-68 "Klik [+ Unit], isi `Mile` / `mi`" dipenuhi dengan form yang sama (langkah 41, 48 dan 23).
- Target Edit TC-GS-UOM-89 dan 90 memakai unit milik spec (`Fail Edit {runId}-023`) menggantikan Liter di TC sumber (S-06). Asersi "Data Liter tidak berubah" (Expected Result c TC-GS-UOM-89) diasersi pada unit milik spec setelah form ditutup (langkah 56).
- Langkah penghubung (aksi tanpa `Verifikasi`): memasang dan melepas intercept (langkah 1, 9, 10, 22, 32, 38, 47, 52, 57, 64), menutup toast error atau koneksi (langkah 21, 27, 46, 51; toast error berulang di-dismiss sebelum diasersi lagi, S-09), langkah 4 (menunggu cek keunikan gagal), langkah 39 dan 58 (Search agar baris target tampil), 35 dan 37 (Search lalu menutup Search), serta langkah 53 dan 55 (menutup form dirty lewat `[✕]` lalu [Leave]; langkah 54 memverifikasi dialog, S-08).
- Parameter: 10 detik pengamatan toast error (langkah 16) adalah parameter pengamatan "tetap tampil sampai di-dismiss", bukan klaim PRD.
- Alasan spec tidak dipecah (68 langkah, melewati batas 35 langkah): satu kelas harness (fault injection dengan intercept parsial), satu akun, dan form yang terbuka dipakai ulang antar-TC (prinsip 6); tiap kelompok (Create, Edit) memakai data sendiri sehingga kegagalan satu kelompok tidak menghilangkan makna kelompok lain, namun memecah akan mengulang pemasangan intercept dan pembukaan form.
- Temuan untuk QA:
  - Mekanisme "timeout" tidak didefinisikan di TC. TC-GS-UOM-343 dan 352 mengharapkan Try Again membuat atau mengubah data sekali tanpa duplikat, sehingga spec mengasumsikan request timeout tidak diteruskan ke server (Prerequisites). Bila timeout meneruskan request ke server (seperti yang terjadi pada Brand), Expected Result "Hanya satu League tersimpan" perlu penyesuaian di TC.
  - Expected Result b TC-GS-UOM-89 ("retry manual tersedia") tidak menyebut elemen yang diamati; spec mengasersi tombol [Save] enabled kembali (langkah 45).
  - TC-GS-UOM-49 tidak menyebut berapa lama cek keunikan "timeout" ditunggu; spec menunggu cek selesai gagal sebelum mengasersi (langkah 4).
  - TC-GS-UOM-67 dan 89 menyebut toast persisten ("tetap tampil sampai di-dismiss") hanya pada TC-GS-UOM-67; toast error TC-GS-UOM-89 tidak diasersi persisten.
  - Endpoint cek keunikan, Create, dan Edit untuk intercept tidak disebut TC; tim FE menyesuaikan dengan `openapi.yaml` modul.
