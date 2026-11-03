---
id: TC-AC-ACC-E2E-112-change-partner-penutupan-dialog-unsaved-changes
title: "Dialog Change Partner: Penutupan lewat [✕] dan Esc, Dialog Unsaved Changes, dan Status [Confirm]"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-957
  - TC-AC-ACC-180
  - TC-AC-ACC-955
  - TC-AC-ACC-956
coverage:
  web: automated
---

# Dialog Change Partner: Penutupan lewat [✕] dan Esc, Dialog Unsaved Changes, dan Status [Confirm]

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (Tabel A3, kelas Residen): C-ROL-4 `PT Mandiri Jaya` (satu-satunya Partner CV Mitra Mandiri, Group Cabang Bekasi). Fixture ini hanya dibaca: tidak ada [Confirm] di spec ini, sehingga relasi tidak berubah dan tidak ada pemulihan data.
- Partner pembanding: `CV Mitra Lestari` (Active, belum terhubung ke `PT Mandiri Jaya`).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-957: Tutup dialog Change Partner tanpa perubahan lewat [✕] dan Esc

1. Ketik Search `PT Mandiri Jaya`, tekan Enter
2. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
3. Klik `[✕]` pada header dialog
4. Verifikasi dialog Change Partner tertutup langsung
5. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul
6. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
7. Tekan Esc
8. Verifikasi dialog Change Partner tertutup langsung
9. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul

### TC-AC-ACC-180: Confirm disabled dan penutupan tanpa Unsaved Changes selama set Partner sama dengan kondisi awal

10. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
11. Verifikasi `[Confirm]` disabled
12. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
13. Verifikasi `[Confirm]` aktif
14. Klik `[Remove]` pada baris "CV Mitra Lestari" (badge `New`)
15. Verifikasi `[Confirm]` disabled
16. Verifikasi list "Current Partners" hanya memuat "CV Mitra Mandiri"
17. Klik `[✕]` pada header dialog
18. Verifikasi dialog Change Partner tertutup langsung
19. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul
20. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
21. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari", lalu klik `[Remove]` pada baris "CV Mitra Lestari" (badge `New`)
22. Tekan Esc
23. Verifikasi dialog Change Partner tertutup langsung
24. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul

### TC-AC-ACC-955: Tutup dialog lewat [✕] dengan Partner baru belum dikonfirmasi: outcome [Cancel] dan [Leave]

25. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
26. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
27. Klik `[✕]` pada header dialog
28. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
29. Klik `[Cancel]` pada dialog Unsaved Changes
30. Verifikasi dialog Unsaved Changes tertutup
31. Verifikasi dialog Change Partner tetap terbuka
32. Verifikasi list "Current Partners" memuat "CV Mitra Mandiri" dan "CV Mitra Lestari" (badge `New`)
33. Klik `[✕]` pada header dialog
34. Klik `[Leave]`
35. Verifikasi dialog Change Partner tertutup
36. Verifikasi tidak ada toast
37. Verifikasi Managed By baris `PT Mandiri Jaya` tetap "CV Mitra Mandiri" tanpa `+1 more`

### TC-AC-ACC-956: Tekan Esc setelah Remove Partner belum dikonfirmasi: [Leave] menutup tanpa menyimpan

38. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
39. Klik `[Remove]` pada "CV Mitra Mandiri"
40. Tekan Esc
41. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
42. Klik `[Leave]`
43. Verifikasi dialog Change Partner tertutup
44. Verifikasi tidak ada toast
45. Verifikasi Managed By baris `PT Mandiri Jaya` adalah "CV Mitra Mandiri"
46. Verifikasi Group baris `PT Mandiri Jaya` adalah "Cabang Bekasi"

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (penutupan dialog Change Partner) satu dataset dan satu akun; tiap blok membuka dialog sendiri dari baris yang sama sehingga tetap bermakna walau blok sebelumnya gagal. Kasus menutup form ditaruh di akhir dan jumlah pembukaan dialog sama dengan jumlah kejadian menutup (prinsip 6).
- Search `PT Mandiri Jaya` diketik sekali di awal sebagai langkah TC (R-16); tabel tidak berubah di antara blok sehingga pembukaan ulang Search tidak diperlukan.
- Langkah penghubung (tanpa awalan Verifikasi): menutup dialog bersih lewat `[✕]` atau Esc dan menutup dialog dirty lewat `[Leave]` merupakan langkah TC (aksi menutup); tidak ada langkah penghubung tambahan.
- Post Condition TC-AC-ACC-957, 180, 955, 956: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-180 langkah 6 menyebut baris "CV Mitra Lestari" (badge `New`) di-Remove tanpa menyebut bahwa dialog masih dalam keadaan tidak dirty setelahnya; spec mengikuti Expected d dan e TC (dialog tertutup langsung tanpa Unsaved Changes).
