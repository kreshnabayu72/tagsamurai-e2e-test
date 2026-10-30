---
id: TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup
title: "Modal Changelog Custom Field: Screening, Tooltip, Hover Modified By, Klik Backdrop dan Esc, Error Load, Loading State, dan Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-253
  - TC-GS-UCF-526
  - TC-GS-UCF-254
  - TC-GS-UCF-255
  - TC-GS-UCF-257
  - TC-GS-UCF-527
  - TC-GS-UCF-269
coverage:
  web: automated
---

# Modal Changelog Custom Field: Screening, Tooltip, Hover Modified By, Klik Backdrop dan Esc, Error Load, Loading State, dan Empty State

## Prerequisites

- Mode: FE+BE (backend nyata; intercept jaringan parsial di atas backend nyata untuk TC-GS-UCF-257 dan TC-GS-UCF-527, tidak mengasersi state backend).
- Akun aktor:
  - Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) untuk seluruh TC kecuali TC-GS-UCF-255. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client C Rudi Hartanto `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup TC; Client C tanpa Custom Field dan tanpa Changelog) untuk TC-GS-UCF-255, login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka kecuali sesudah ganti akun.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A (`Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date`) dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (fixture backend). Entri Delete `Legacy Field` termasuk di dalamnya.
- Data Population (precondition TC): 8 Custom Field `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number` dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent, dilewati bila sudah ada; menghasilkan 8 entri Create dengan Modified By `Sari D`). Total 14 Custom Field dan 16 entri Changelog Client A. Dipakai sebagai precondition TC, tidak diasersi satu per satu.
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (Sari Dewi dan Rudi Hartanto) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover untuk tooltip; klik area backdrop di luar modal; tombol Esc; ganti akun (logout lalu login); intercept jaringan pada respons list Changelog Custom Field (`POST /v2/activity-logs/changelogs/list` dengan `logTable: "Custom Field"` dan `product: "global_settings"`; layanan activity-log, low-level-design.md:7; tidak ada di openapi.yaml modul): memaksa respons 500 (TC-GS-UCF-257) dan menahan respons 3 detik (TC-GS-UCF-527), keduanya dilepas segera setelah pemicu selesai.
- State global: tidak ada yang diubah selain flag Guided Tooltip, sesi akun, dan intercept (dilepas seperti di atas).

## Test Steps

### TC-GS-UCF-253: Screening Modal Changelog Custom Field

1. Klik icon Changelog
2. Verifikasi Header: Title `Changelog: Custom Field`
3. Verifikasi Header: `[✕]`
4. Verifikasi Header: toolbar `Search | Filter | Download`
5. Verifikasi Body: urutan kolom `Date | Action | Field | Old Value | New Value | Modified By | Column Visibility (⋯)`
6. Verifikasi Body: kolom Date sortable
7. Verifikasi Body: kolom Action sortable
8. Verifikasi Body: kolom Field sortable
9. Verifikasi Body: kolom Old Value sortable
10. Verifikasi Body: kolom New Value sortable
11. Verifikasi Body: kolom Modified By sortable
12. Verifikasi Body: kolom `Column Visibility (⋯)` unsortable
13. Verifikasi Body: urut Date terbaru di atas
14. Verifikasi Body: Action berupa plain text (bukan badge)
15. Verifikasi Body: Old Value entri Create `-`
16. Verifikasi Body: New Value entri Delete `-`
17. Verifikasi Body: tidak ada entri dengan Old Value dan New Value keduanya `-`
18. Verifikasi Body: Modified By berformat `[First Name] [Last Initial]`
19. Verifikasi Body: Modified By plain text tanpa avatar
20. Verifikasi Footer: Pagination default 10
21. Verifikasi Footer: Pagination menawarkan opsi 10/25/50/100

### TC-GS-UCF-526: Tooltip icon toolbar dan header kolom Actions

22. Hover icon Search
23. Verifikasi tooltip `Search`
24. Hover icon Filter
25. Verifikasi tooltip `Filter`
26. Hover icon Download
27. Verifikasi tooltip `Download`
28. Hover header kolom Column Visibility (⋯)
29. Verifikasi tooltip `Column Visibility`

### TC-GS-UCF-269: Hover Modified By menampilkan nama lengkap

30. Hover `Budi S` pada baris Create `Cost Center`
31. Verifikasi tooltip `Budi Santoso`

### TC-GS-UCF-254: Modal Changelog hanya ditutup lewat Esc, klik backdrop diabaikan

32. Klik backdrop di luar modal
33. Verifikasi Modal Changelog tetap terbuka (klik backdrop tidak menutup modal)
34. Tekan Esc
35. Verifikasi Modal Changelog tertutup

### TC-GS-UCF-257: Error load Modal Changelog

36. Paksa respons list Changelog Custom Field menjadi 500 (intercept)
37. Klik icon Changelog
38. Verifikasi pesan `Unable to load this data.` tampil
39. Verifikasi `[Try Again]` tampil
40. Lepas intercept (pulihkan respons)
41. Klik `[Try Again]`
42. Verifikasi entri Changelog termuat (sedikitnya satu baris entri tampil)
43. Klik `[✕]`

### TC-GS-UCF-527: Loading state Modal Changelog saat entri dimuat

44. Tunda respons list Changelog Custom Field selama 3 detik (intercept)
45. Klik icon Changelog
46. Verifikasi komponen loading tampil di area tabel modal selama respons tertunda
47. Verifikasi empty state `No changelog yet` tidak tampil selama loading
48. Verifikasi pesan error tidak tampil selama loading
49. Verifikasi komponen loading hilang setelah respons diterima
50. Verifikasi entri Changelog tampil setelah respons diterima
51. Lepas intercept
52. Klik `[✕]`

### TC-GS-UCF-255: Empty state Changelog saat belum ada aktivitas (Client C)

53. Ganti akun: logout dari Total Control Client A Sari Dewi
54. Login sebagai Total Control Client C Rudi Hartanto (`Spectra.env.GS_CLIENTC_TC_PASSWORD`)
55. Buka Global Settings > User > Custom Field
56. Klik icon Changelog
57. Verifikasi Illustration tampil
58. Verifikasi Title `No changelog yet`
59. Verifikasi Description `Activities and changes will appear here.`
60. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 253, 526, 269, 254, 257, 527, 255. Screening, tooltip, dan hover dikerjakan pada satu pembukaan modal (langkah 1); kasus menutup (254) ditaruh sesudahnya; kasus intercept (257, 527) sesudah kasus yang memakai data normal; TC-GS-UCF-255 di akhir karena berganti akun ke Client C (konvensi bagian 3 prinsip 2, 3, dan 6). Modal dibuka empat kali (langkah 1, 37, 45, 56) dan ditutup empat kali (langkah 34, 43, 52, 60); kasus 254 memakai pembukaan langkah 1 dan ditutup dengan Esc.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 36 dan 44 (memasang intercept), langkah 40 dan 51 (melepas intercept, S-09), langkah 43 dan 52 dan 60 (menutup modal lewat `[✕]`; modal tidak memuat form sehingga tanpa dialog), langkah 53 sampai 55 (ganti akun dan buka tab Custom Field). Absence loading state (langkah 47 dan 48) diletakkan segera sesudah pemicu dan sesudah `Verifikasi` komponen loading sebagai anchor positif (bagian 8b butir 2, 5, dan 11).
- Spec melewati sekitar 35 langkah (60 langkah). Seluruhnya satu kelas ringan (tampilan Modal Changelog, hanya membaca, tanpa aksi yang mengubah data; intercept hanya sebagai pemicu state UI loading dan error, P-2). Tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; ganti akun di langkah 53 memiliki langkah eksplisit dan bagian sesudahnya (entitas Client C) tetap bermakna walau bagian sebelumnya gagal.
- Topik satu dataset Changelog (screening 061, Search 062, Filter 063, Sort dan Pagination 064, Setup Column 065, Download 066) dipertahankan sebagai spec terpisah karena gabungannya melewati batas ukuran jauh dan tiap spec menyiapkan datanya sendiri.
- TC yang terbelah: Expected pencatatan log ada di spec 067 sampai 070; format tanggal Modal Changelog ada di spec 071.
- Temuan untuk QA:
  - TC-GS-UCF-253 sampai 255 dan 257: precondition d mengasumsikan Changelog Client A hanya memuat 8 entri Pre-setup dan 8 entri Create Population; tiap spec lain di Client A menulis entri Changelog permanen (audit trail), sehingga asersi yang bergantung pada total entri hanya bermakna bila lingkungan automation bersih. Spec ini tidak mengasersi total entri.
  - TC-GS-UCF-253 menulis token sel kosong `-` (hyphen), sedangkan TC-GS-UCF-283, 338, dan 380 menulis `—` (em dash) untuk nilai kosong Changelog yang sama. Spec mengikuti masing-masing TC; mohon QA menetapkan satu token.
  - TC-GS-UCF-254 berjudul "hanya ditutup lewat [✕] atau Esc", tetapi langkah dan Expected hanya memuat klik backdrop dan Esc; `[✕]` tidak diasersi di blok ini (menutup lewat `[✕]` hanya sebagai langkah penghubung blok 257, 527, dan 255).
  - TC-GS-UCF-255 menyebut akun Client C tanpa email di Pre-setup yang eksplisit (email diambil dari baris `Total Control Client C` Pre-setup TC) dan tanpa env var password; spec memakai `GS_CLIENTC_TC_PASSWORD` yang sudah terdaftar di `spectra.config.ts` dan `.env.example`.
  - Nilai 3 detik (TC-GS-UCF-527) bertanda `PRD?` di TC; spec mengikuti TC sebagai penahanan respons lewat intercept.
  - TC-GS-UCF-257 dan 527 tidak menyebut endpoint yang di-intercept; spec menyebut respons list Changelog Custom Field `POST /v2/activity-logs/changelogs/list` (low-level-design.md:7).
