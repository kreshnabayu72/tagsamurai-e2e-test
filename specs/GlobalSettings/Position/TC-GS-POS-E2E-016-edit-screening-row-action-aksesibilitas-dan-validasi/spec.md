---
id: TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi
title: "Edit Position: Overlay Row Action, Screening Form, Aksesibilitas, Validasi Inline, Clear Field, dan Hover Tombol"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-74
  - TC-GS-POS-75
  - TC-GS-POS-76
  - TC-GS-POS-77
  - TC-GS-POS-78
  - TC-GS-POS-80
  - TC-GS-POS-81
  - TC-GS-POS-82
  - TC-GS-POS-83
  - TC-GS-POS-88
  - TC-GS-POS-285
coverage:
  web: automated
---

# Edit Position: Overlay Row Action, Screening Form, Aksesibilitas, Validasi Inline, Clear Field, dan Hover Tombol

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`.
- Data Pre-setup (tidak diubah spec ini, tanpa suffix): Position 11 `Finance Analyst` (bebas relasi), dipakai sebagai nama pembanding duplikat pada TC-GS-POS-88 (nilai yang diketik `finance analyst`).
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.editSeed016`): satu Position `Legal Counsel {runId}-016` (milik spec ini; tidak pernah disimpan ulang, nama tidak berubah). Nilai uji yang diketik namun tidak tersimpan: 3 spasi; nama 121 karakter `Senior Manager of Regional Supply Chain Planning, Procurement Strategy, Vendor Performance and Logistics Cost ProgramsssX`; nama 119 karakter `Senior Manager of Regional Supply Chain Planning, Procurement Strategy, Vendor Performance and Logistics Cost Programss` ditambah 2 spasi di akhir; emoji 🚀; clipboard `Legal 🚀 Counsel`; `finance analyst`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Position `Legal Counsel {runId}-016` bila masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: membaca atribut ARIA (`aria-required`, `aria-describedby`) pada input; input keyboard (Tab berulang, mengetik emoji, paste dari clipboard); hover pada tombol; membaca warna border dan state fokus; membaca ikon dan severity opsi overlay.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-POS-74: Screening Overlay Row Action pada baris Position

1. Ketik Search `Legal Counsel {runId}-016`, tekan Enter
2. Klik `⋯` pada baris `Legal Counsel {runId}-016`
3. Verifikasi Overlay Row Action menempel pada `⋯`
4. Verifikasi Overlay Row Action tanpa backdrop
5. Verifikasi opsi berurutan `Edit` lalu `Delete`
6. Verifikasi opsi `Edit` memakai icon Edit2Line
7. Verifikasi opsi `Edit` berseverity dark
8. Verifikasi opsi `Delete` memakai icon DeleteBin6Line
9. Verifikasi opsi `Delete` berseverity danger

### TC-GS-POS-75: Screening Popup Edit Position, 3 zona

10. Klik `Edit` pada Overlay Row Action
11. Verifikasi Popup Edit Position terbuka
12. Verifikasi Header menampilkan Title "Edit Position"
13. Verifikasi Header memiliki icon `[✕]`
14. Verifikasi Body menampilkan Label "Position Name *"
15. Verifikasi input Position Name pre-filled `Legal Counsel {runId}-016`
16. Verifikasi kursor fokus di input Position Name
17. Verifikasi tidak ada checkbox "Stay on this form after submitting"
18. Verifikasi `[Clear Field]` di Footer bergaya text (primary)
19. Verifikasi `[Save]` di Footer bergaya filled (success)
20. Verifikasi urutan tombol di Footer `[Clear Field]` lalu `[Save]`
21. Verifikasi tombol Footer rata kanan
22. Verifikasi tidak ada `[Cancel]` di Footer

### TC-GS-POS-285: Feedback hover tombol Save dan Clear Field

23. Hover `[Save]`
24. Verifikasi `[Save]` menampilkan background success hover
25. Hover `[Clear Field]`
26. Verifikasi `[Clear Field]` menampilkan state hover text primary

### TC-GS-POS-77: Position Name dikosongkan saat Save

27. Hapus seluruh teks Position Name
28. Klik `[Save]`
29. Verifikasi error inline "Position Name must not be empty"
30. Verifikasi input Position Name berborder danger
31. Verifikasi Popup Edit tetap terbuka
32. Verifikasi tidak ada toast

### TC-GS-POS-76: Accessibility Popup Edit Position, aria-required, aria-describedby, dan focus trap

33. Verifikasi input Position Name memiliki `aria-required="true"`
34. Verifikasi input Position Name memiliki `aria-describedby` yang menunjuk ke elemen pesan error "Position Name must not be empty"
35. Tekan Tab berulang kali melewati seluruh elemen fokus pada popup
36. Verifikasi fokus Tab berputar di dalam popup Edit
37. Verifikasi fokus Tab tidak keluar ke halaman di belakang popup

### TC-GS-POS-78: Position Name hanya spasi saat Save

38. Ketik ulang `Legal Counsel {runId}-016` pada input Position Name
39. Ganti nilai dengan 3 spasi
40. Klik `[Save]`
41. Verifikasi error inline "Position Name must not be empty"
42. Verifikasi Popup Edit tetap terbuka
43. Verifikasi tidak ada toast

### TC-GS-POS-80: Position Name 121 karakter memunculkan error langsung

44. Ketik ulang `Legal Counsel {runId}-016` pada input Position Name
45. Ganti nilai dengan nama 121 karakter (tanpa blur)
46. Verifikasi error inline "Max. 120 characters" muncul langsung saat karakter ke-121 diketik
47. Klik `[Save]`
48. Verifikasi Popup Edit tetap terbuka
49. Verifikasi tidak ada toast sukses

### TC-GS-POS-81: Batas 120 karakter dihitung sebelum trim

50. Ketik ulang `Legal Counsel {runId}-016` pada input Position Name
51. Ganti nilai dengan 119 karakter ditambah 2 spasi di akhir
52. Verifikasi error inline "Max. 120 characters" muncul langsung

### TC-GS-POS-82: Mengetik emoji pada Position Name

53. Ketik ulang `Legal Counsel {runId}-016` pada input Position Name
54. Letakkan kursor di akhir teks, ketik emoji 🚀
55. Verifikasi emoji tidak masuk ke nilai field
56. Verifikasi nilai field tetap `Legal Counsel {runId}-016`
57. Verifikasi tidak ada pesan error inline

### TC-GS-POS-83: Paste teks berisi emoji pada Position Name

58. Ganti nilai dengan paste `Legal 🚀 Counsel`
59. Verifikasi emoji tidak masuk ke nilai field
60. Verifikasi sisa teks tanpa emoji (`Legal` dan `Counsel`) tetap masuk ke nilai field
61. Verifikasi tidak ada pesan error inline "Position Name contains invalid characters"

### TC-GS-POS-88: Clear Field mengosongkan field, bukan revert

62. Ketik ulang `Legal Counsel {runId}-016` pada input Position Name
63. Ganti nilai dengan `finance analyst`
64. Verifikasi error inline "Position Name already exists" tampil
65. Klik `[Clear Field]`
66. Verifikasi Position Name kosong (`""`)
67. Verifikasi Position Name tidak kembali ke `Legal Counsel {runId}-016`
68. Verifikasi error inline hilang
69. Verifikasi border danger hilang
70. Verifikasi Popup Edit tetap terbuka
71. Verifikasi fokus di input Position Name
72. Verifikasi dialog Unsaved Changes tidak muncul

### Penutupan form

73. Klik `✕` pada Popup Edit
74. Verifikasi dialog Unsaved Changes muncul (field kosong berbeda dari nilai tersimpan)
75. Klik `[Leave]`
76. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 74, 75, 285, 77, 76, 78, 80, 81, 82, 83, 88. TC-GS-POS-285 (hover) ditaruh tepat sesudah TC-GS-POS-75 karena hover diamati pada form yang belum diubah. TC-GS-POS-77 mendahului TC-GS-POS-76 karena aksi "kosongkan lalu `[Save]`" (langkah 27 sampai 28) dipakai bersama; error inline harus sudah tampil sebelum `aria-describedby` diperiksa, dan asersi "tidak ada toast" (langkah 32) harus dibuat sebelum langkah berikutnya. TC-GS-POS-88 terakhir karena `[Clear Field]` membuat form dirty. Urutan menyimpang dari urutan TC sumber.
- Satu popup Edit dipakai untuk seluruh TC (satu pembukaan, satu penutupan: langkah 10 dan 73 sampai 75). Langkah 2 dan 10 (`⋯` lalu `Edit`) dipakai bersama TC-GS-POS-74 dan TC-GS-POS-75.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search agar baris target tampil pada halaman aktif), langkah 38, 44, 50, 53, 62 (mengetik ulang nilai tersimpan agar error dari TC sebelumnya hilang dan tiap TC dimulai dari nilai awal), langkah 73 dan 75 (aksi penutupan form dirty; langkah 74 adalah `Verifikasi` dialog tambahan agar penutupan deterministik, S-08), dan langkah 76 (menutup input Search dan mereset tabel). Langkah 39, 45, 51, 58, dan 63 adalah langkah TC.
- Langkah 11 adalah `Verifikasi` dari anotasi "→ Popup Edit Position terbuka" pada Langkah 1 TC-GS-POS-75.
- Langkah 64 menambahkan `Verifikasi` error duplikat "Position Name already exists" sebagai pembentuk state awal untuk Expected b TC-GS-POS-88 ("error inline dan border danger hilang"); TC menyebut error tersebut hanya pada Langkah dan tidak pada Expected.
- Nama record memakai suffix `{runId}-016`; Expected TC yang menyebut `Legal Counsel` diasersi dengan nama bersuffix tersebut.
- Spec melewati sekitar 35 langkah (76 langkah). Seluruhnya satu kelas (Edit: tampilan, aksesibilitas, validasi inline tanpa Save sukses), satu akun, satu record milik spec, dan tidak ada aksi yang mengubah data; tiap blok validasi dimulai dari nilai tersimpan yang diketik ulang. Kegagalan keras pada pembukaan popup menghentikan seluruh blok.
- Temuan untuk QA:
  - Post Condition "Nama record tetap `Legal Counsel`" (TC-GS-POS-77, 78, 80) tanpa langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-75 menulis footer tanpa `[Cancel]`; sesuai konvensi §24.1 dan NC-09.
  - TC-GS-POS-80 Expected a menyebut error muncul "langsung saat karakter ke-121 diketik" sedangkan Langkah 3 mengklik `[Save]` untuk Expected b; spec mengasersi error sebelum `[Save]` dan penolakan sesudahnya.
  - TC-GS-POS-83 tidak menyebut nilai akhir field; spec mengasersi bahwa `Legal` dan `Counsel` tetap ada dan emoji tidak ada, tanpa mengasersi jumlah spasi.
  - TC-GS-POS-88 Langkah 2 ("hingga error duplikat tampil") tidak punya Expected untuk error tersebut; lihat catatan langkah 64.
