---
id: TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout
title: "Dialog Change Partner: Screening, Opsi [+ Add Partner], Badge Status Partner, dan Callout Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-174
  - TC-AC-ACC-508
  - TC-AC-ACC-597
  - TC-AC-ACC-995
  - TC-AC-ACC-596
  - TC-AC-ACC-595
coverage:
  web: automated
---

# Dialog Change Partner: Screening, Opsi [+ Add Partner], Badge Status Partner, dan Callout Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (Tabel A2/A3), semuanya hanya dibaca dan tidak dikonfirmasi: C-02 `PT Teknologi Maju` (Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari); C-13 `PT Ganti Mitra` (hanya CV Mitra Sejati); C-ROL-9 `PT Relasi Campur` (relasi CV Mitra Sejati Active dan CV Mitra Beku Suspended); C-ROL-8 `PT Ubah Mitra 07` (satu-satunya Partner CV Mitra Sejati); Partner P-ROL-2 `CV Mitra Beku` (Suspended) dan Partner Active lain `CV Mitra Lestari`, `CV Mitra Timur`, `CV Mitra Mandiri`.
- Tidak ada [Confirm] pada dialog di spec ini, sehingga tidak ada relasi Partner yang berubah dan tidak ada pemulihan data selain menutup dialog.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-174: Screening Dialog Change Partner

1. Ketik Search `PT Teknologi Maju`, tekan Enter
2. Klik `[⋯]` pada baris `PT Teknologi Maju` → klik `Change Partner`
3. Verifikasi header dialog berjudul "Change Partner" dengan tombol `[✕]`
4. Verifikasi list "Current Partners" memuat "CV Mitra Sejati" dan "CV Mitra Lestari", masing-masing dengan badge `Active`
5. Verifikasi baris Partner tanpa drag handle
6. Verifikasi tiap baris Partner memiliki tombol `[Remove]`
7. Verifikasi `[+ Add Partner]` berupa multi-select
8. Verifikasi field `[Group]` read-only
9. Verifikasi callout "Group is inherited from the topmost partner — drag to reorder if you need a different partner to determine the group."
10. Verifikasi footer memuat `[Clear Field]` dan `[Confirm]`
11. Verifikasi `[Confirm]` disabled (belum ada perubahan)
12. Verifikasi lebar dialog 560px
13. Klik `[✕]` pada header dialog

### TC-AC-ACC-508: Dialog Change Partner oleh Principal: opsi [+ Add Partner] memuat seluruh Partner

14. Ketik Search `PT Ganti Mitra`, tekan Enter
15. Klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`
16. Verifikasi list "Current Partners" hanya memuat "CV Mitra Sejati"
17. Verifikasi baris "CV Mitra Sejati" tanpa badge `New`
18. Verifikasi `[+ Add Partner]` tanpa Partner terpilih
19. Verifikasi `[Confirm]` disabled
20. Buka dropdown `[+ Add Partner]`
21. Verifikasi opsi memuat "CV Mitra Lestari" dan "CV Mitra Timur"
22. Tutup dropdown dengan klik area kosong di dalam dialog
23. Klik `[✕]` pada header dialog

### TC-AC-ACC-597 dan TC-AC-ACC-995: Badge status Partner dan opsi [+ Add Partner] pada Client dengan relasi Suspended

24. Ketik Search `PT Relasi Campur`, tekan Enter
25. Klik `[⋯]` pada baris `PT Relasi Campur` → klik `Change Partner`
26. Verifikasi list "Current Partners" memuat "CV Mitra Sejati" dengan badge `Active` dan "CV Mitra Beku" dengan badge `Suspended`
27. Verifikasi kedua baris memiliki tombol `[Remove]`
28. Verifikasi kedua baris tanpa drag handle
29. Klik `[+ Add Partner]`
30. Verifikasi opsi memuat "CV Mitra Lestari" (Active, belum terhubung)
31. Verifikasi opsi tidak memuat "CV Mitra Sejati" (sudah terhubung, Active)
32. Verifikasi opsi tidak memuat "CV Mitra Beku" (sudah terhubung, Suspended)
33. Tutup dropdown dengan klik area kosong di dalam dialog
34. Klik `[✕]` pada header dialog

### TC-AC-ACC-596: Principal membuka [+ Add Partner]: opsi mencakup Partner lintas jaringan

35. Ketik Search `PT Ubah Mitra 07`, tekan Enter
36. Klik `[⋯]` pada baris `PT Ubah Mitra 07` → klik `Change Partner`

### TC-AC-ACC-595: Callout Select Group menggantikan callout Group inherited dan kembali bila Partner ditambahkan lagi

37. Verifikasi field `[Group]` read-only dengan callout "Group is inherited from the topmost partner — drag to reorder if you need a different partner to determine the group."

### TC-AC-ACC-596 (lanjutan)

38. Klik `[+ Add Partner]`
39. Verifikasi opsi memuat "CV Mitra Lestari" (jaringan PT Distribusi Nusantara), "CV Mitra Timur" (jaringan PT Distribusi Timur), dan "CV Mitra Mandiri" (tanpa Distributor induk)
40. Verifikasi opsi tidak memuat "CV Mitra Sejati" (sudah terhubung)
41. Verifikasi opsi tidak memuat "CV Mitra Beku" (Suspended)
42. Tutup dropdown dengan klik area kosong di dalam dialog

### TC-AC-ACC-595 (lanjutan)

43. Klik `[Remove]` pada "CV Mitra Sejati"
44. Verifikasi field `[Group]` diganti `Select Group*` dengan callout "This client has no partner and requires a group to be selected manually."
45. Verifikasi callout "Group is inherited from the topmost partner — drag to reorder if you need a different partner to determine the group." tidak tampil
46. Verifikasi `[Confirm]` disabled
47. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
48. Verifikasi field `[Group]` read-only tampil lagi menggantikan `Select Group*`
49. Verifikasi callout "Group is inherited from the topmost partner — drag to reorder if you need a different partner to determine the group." tampil
50. Verifikasi callout "This client has no partner and requires a group to be selected manually." tidak tampil
51. Verifikasi `[Confirm]` aktif tanpa memilih Group
52. Klik `[✕]` pada header dialog
53. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil
54. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas enam TC satu topik (isi dan opsi dialog Change Partner sebelum Confirm), satu akun, tanpa mengubah data; tiap blok membuka dialog dari Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal.
- Pembagian TC lintas blok: TC-AC-ACC-596 dan TC-AC-ACC-595 memakai dataset `PT Ubah Mitra 07` dan satu pembukaan dialog. Langkah 37 (Expected a TC-AC-ACC-595, state awal dialog) ditaruh sebelum langkah 38 sampai 42 (TC-AC-ACC-596) karena opsi "CV Mitra Sejati sudah terhubung" hanya benar selama Partner itu belum di-Remove; langkah 43 sampai 51 (TC-AC-ACC-595 sisanya) harus sesudahnya (butir 5 bagian 8b: urutan langkah mengikuti urutan state). TC-AC-ACC-597 dan TC-AC-ACC-995 berbagi satu pembukaan dialog karena tidak mengubah state.
- Langkah penghubung (tanpa awalan Verifikasi): menutup dropdown dan menutup dialog bersih lewat `[✕]` (langkah 13, 23, 34), serta menutup dialog dirty lewat `[✕]` dan `[Leave]` di akhir spec (langkah 52 dan 54; `Verifikasi` dialog Unsaved Changes pada langkah 53 diwajibkan S-08).
- Search dipakai untuk menemukan baris target (R-16): langkah 1, 14, 24, 35 adalah langkah TC (isi kotak Search diganti oleh Search berikutnya).
- Post Condition TC-AC-ACC-174, 508, 596, 597, 995: `-`. Tidak ada Post Condition dengan Expected yang tidak diobservasi.
- Temuan untuk QA:
  - TC-AC-ACC-595 tidak menyebut cara menutup dialog yang berakhir dirty; spec menutupnya lewat `[✕]` lalu `[Leave]` (S-08, S-09).
  - TC-AC-ACC-174 Expected b menyebut "Group is inherited from the topmost partner" sebagai callout sedangkan Expected 508 tidak menyinggung callout; spec tidak mengasersi callout pada langkah blok 508 karena tidak ada Expected-nya.
