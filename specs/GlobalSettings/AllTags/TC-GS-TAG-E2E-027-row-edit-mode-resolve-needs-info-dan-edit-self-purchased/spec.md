---
id: TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased
title: "Row Edit Mode: Resolve Needs Info, Validasi Save, Edit Self-Purchased, Kontrol Lain Nonaktif, Cancel, dan Unsaved Changes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-77
  - TC-GS-TAG-78
  - TC-GS-TAG-79
  - TC-GS-TAG-80
  - TC-GS-TAG-81
  - TC-GS-TAG-82
  - TC-GS-TAG-83
  - TC-GS-TAG-355
coverage:
  web: automated
---

# Row Edit Mode: Resolve Needs Info, Validasi Save, Edit Self-Purchased, Kontrol Lain Nonaktif, Cancel, dan Unsaved Changes

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Stok resmi Admin Console Client A (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`) di-seed idempotent oleh fixture BE di hook `before`: GPS `356938035643001` (DD-S1) Available. Akun Admin Console untuk seeding stok disediakan tim FE (S-13).
- Data identifier: `356938035643101` (DD-N1) dan `356938035643102` (DD-N2) tidak ada di stok resmi dan tidak ada di registri Client A. Opsi mandiri (BYO) aktif; Template Self-Purchased kosong pada awal tiap sesi kecuali disebut.
- Data Dinamis TC-355 (milik spec ini, bersufiks): Device Name `Pelacak Uji Hapus {runId}-027` (Category `GPS`, Measurement `Unit`, tanpa SKU dan tanpa unit) di-seed oleh Total Control entitas Principal lewat sesi API di hook `before` dan dibersihkan di hook `after` bila masih ada. Akun Principal pelaku modul Device Name tidak ada di Pre-setup TC: disediakan tim FE (S-13, Q-2; Pre-setup TC memuat `principalApprover_automated@qwertysystem.net` dengan env `GS_PRINCIPAL_TC_PASSWORD`, tetapi akun modul Device Name tidak ditetapkan).
- Pemicu kedua (P-2): penghapusan Device Name oleh Principal di Settings > Device > Device Name memakai sesi API (bukan sesi UI kedua) karena hanya berfungsi sebagai pemicu state; langkah 60 menulisnya "hingga tersimpan".
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE sesuai plan bagian 6) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Sesi 1 (Template kosong)

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` tanpa Template

### TC-GS-TAG-78: Save dengan Device Name kosong

3. Klik `Resolve` pada baris `356938035643101`
4. Isi Brand `Queclink`, biarkan Device Name kosong
5. Klik `Save`
6. Verifikasi error inline pada Device Name `Device name is required.`
7. Verifikasi baris `356938035643101` tetap `Needs Info`
8. Verifikasi mode edit tetap aktif

### TC-GS-TAG-79: Save dengan Brand dan SKU kosong

9. Isi Device Name `Queclink GV300`, kosongkan Brand, biarkan SKU kosong
10. Pindahkan fokus keluar dari field Brand tanpa mengklik `Save`
11. Verifikasi belum ada error inline pada Brand (error tidak muncul saat field kehilangan fokus)
12. Klik `Save`
13. Verifikasi error inline pada Brand `Brand is required when SKU is empty.`

### TC-GS-TAG-77: Resolve Needs Info menjadi Self-Purchased

14. Verifikasi sel Device Name, SKU, Brand, dan Model/Type menjadi input aktif inline (bukan dialog)
15. Verifikasi footer mode edit `Cancel | Clear Field | Save`
16. Isi sel Device Name `Queclink GV300` dan Brand `Queclink`
17. Klik `Save`
18. Verifikasi baris `356938035643101` berstatus `Self-Purchased` dengan Device Name `Queclink GV300` dan Brand `Queclink`
19. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 2 (Template terisi)

20. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
21. Buka section `Self-Purchased Template`
22. Isi Template Device Name `Queclink GV300`, SKU kosong, Brand `Queclink`, Model/Type `GV300`

### TC-GS-TAG-80: Edit baris Self-Purchased memakai Row Edit Mode; baris Official tanpa Edit

23. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` lalu `356938035643001` (`356938035643101` Self-Purchased, `356938035643001` Official)
24. Klik `Edit` pada baris `356938035643101`
25. Ubah Model/Type menjadi `GV350`
26. Klik `Save`
27. Verifikasi baris `356938035643101` menampilkan Model/Type `GV350`
28. Verifikasi aksi baris `356938035643001` (Official) hanya `Remove`
29. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 3 (Template kosong)

30. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
31. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` lalu `356938035643102` tanpa Template

### TC-GS-TAG-81: Kontrol lain nonaktif selama Row Edit Mode

32. Klik `Resolve` pada baris `356938035643101`
33. Hover kontrol unggah berkas (`Upload`)
34. Verifikasi tooltip `Finish or cancel the current edit first.` pada kontrol unggah berkas
35. Verifikasi kontrol unggah berkas nonaktif
36. Hover kontrol entri manual (`Manual Entry`)
37. Verifikasi tooltip `Finish or cancel the current edit first.` pada kontrol entri manual
38. Verifikasi kontrol entri manual nonaktif
39. Verifikasi row action baris `356938035643102` nonaktif
40. Verifikasi checkbox baris `356938035643102` nonaktif

### TC-GS-TAG-82: Cancel tanpa perubahan

41. Klik `Cancel` pada footer mode edit
42. Verifikasi mode edit selesai tanpa dialog
43. Verifikasi baris `356938035643101` tetap `Needs Info`

### TC-GS-TAG-83: Cancel dengan perubahan memunculkan dialog Unsaved Changes

44. Klik `Resolve` pada baris `356938035643101`
45. Isi Device Name `Queclink GV300`
46. Klik `Cancel` pada footer
47. Verifikasi dialog dengan body `You have unsaved changes. Are you sure you want to leave?`
48. Verifikasi dialog memiliki tombol `Cancel` dan `Leave`
49. Klik `Cancel` pada dialog
50. Verifikasi dialog tertutup
51. Verifikasi mode edit tetap aktif dengan input `Queclink GV300`
52. Klik `Cancel` pada footer lagi, lalu klik `Leave`
53. Verifikasi mode edit berakhir
54. Verifikasi baris `356938035643101` tetap `Needs Info` tanpa nilai yang diisi
55. Kembali ke List: klik item sidebar `TAG` (staging kosong)

### Sesi 4 (Template kosong)

56. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
57. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` tanpa Template

### TC-GS-TAG-355: Device Name dihapus dari katalog saat Row Edit Mode

58. Klik `Resolve` pada baris `356938035643101`
59. Pilih Device Name `Pelacak Uji Hapus {runId}-027` dan isi Brand `Queclink` (belum `Save`)
60. Principal menghapus Device Name `Pelacak Uji Hapus {runId}-027` di Settings > Device > Device Name hingga tersimpan (sesi API, akun disediakan tim FE)
61. Klik `Save`
62. Verifikasi error inline pada Device Name `Device name is required.`
63. Verifikasi baris `356938035643101` tetap `Needs Info`
64. Verifikasi mode edit tetap aktif
65. Verifikasi Brand `Queclink` tetap terisi
66. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (Row Edit Mode pada staging GPS).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah (66 langkah): semua blok satu kelas harness (Row Edit Mode pada halaman Activate GPS), empat sesi berdiri sendiri sehingga kegagalan satu sesi tidak membuat sesi lain kehilangan makna; di dalam sesi 1 dan sesi 3 blok TC berurutan memakai baris yang sama, sehingga kegagalan keras Row Edit Mode (mode edit tidak terbuka) membuat blok sesudahnya dalam sesi itu kehilangan makna dan diterima demi menghindari pembukaan sesi berulang. Pemicu sesi API Principal pada TC-355 hanya sebagai pemicu state (P-2), bukan objek asersi.
- Urutan sesi 1: kasus ditolak lebih dulu (TC-78, TC-79), lalu sukses (TC-77) pada baris `356938035643101` yang sama; mode edit dibuka pada langkah `Resolve` TC-78 dan diteruskan ke TC-79 dan TC-77 (TC-77 langkah 5 "Klik `Resolve`" dan TC-78/TC-79 langkah 5 dipenuhi satu klik `Resolve`). TC-77 Expected a (input inline dan footer) diasersi pada mode edit yang sama sebelum `Save` sukses. Sesi 3 memakai satu pasang baris untuk TC-81, TC-82, dan TC-83.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Pindahkan fokus keluar` pada TC-79 menjalankan TC Expected b (error muncul saat `Save`, bukan saat fokus hilang) dan diasersi sebelum `Save`; `Kembali ke List` dengan `Leave` hanya bila staging berisi baris adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini (`Leave` tanpa `Verifikasi` dialog).
- Temuan untuk QA:
  - TC-81 menulis tombol toolbar `Upload`/`Manual Entry`/`Remove` dan `Scan TAG` pada sesi GPS, sedangkan sesi GPS tidak memiliki `Scan TAG` maupun `Remove` scan-based (TC-44 Expected c) dan label kontrol unggah/entri manual menunggu desain (NC-11); spec mengasersi hanya kontrol unggah berkas dan entri manual.
  - TC-355 Pre-setup menyebut Total Control entitas Principal dengan "akun fixture modul Device Name" yang tidak terdaftar di Pre-setup TC; Pre-setup TC memuat `principalApprover_automated@qwertysystem.net` (Approvals) dan `.env.example` memuat `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Q-2). Akun disediakan tim FE.
  - TC-355 Device Name `Pelacak Uji Hapus` ditulis literal di TC; spec memakai `Pelacak Uji Hapus {runId}-027` (Data Dinamis bersufiks, S-12).
  - TC-81 Expected ("Row action dan checkbox baris lain nonaktif") diasersi pada baris `356938035643102`; TC tidak menyebut baris tertentu.
