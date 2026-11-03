---
id: TC-AC-ACC-E2E-113-change-partner-clear-field-select-group-wajib-drag
title: "Dialog Change Partner: Select Group Wajib Setelah Partner Terakhir di-Remove, Partner Ketiga, Aturan Drag, dan [Clear Field]"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-456
  - TC-AC-ACC-457
  - TC-AC-ACC-179
  - TC-AC-ACC-985
coverage:
  web: automated
---

# Dialog Change Partner: Select Group Wajib Setelah Partner Terakhir di-Remove, Partner Ketiga, Aturan Drag, dan [Clear Field]

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup, hanya dibaca (tidak ada [Confirm] di spec ini, relasi tidak berubah): C-ROL-4 `PT Mandiri Jaya` (satu-satunya Partner CV Mitra Mandiri, Group Cabang Bekasi); C-02 `PT Teknologi Maju` (Anchor CV Mitra Sejati + CV Mitra Lestari); C-13 `PT Ganti Mitra` (hanya CV Mitra Sejati). Partner pembanding Active: `CV Mitra Lestari`, `CV Mitra Mandiri`. Node Group `Cabang Menteng` ada di tree Select Group.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-456: Confirm disabled sampai Select Group terisi setelah Partner terakhir di-Remove (Direct)

1. Ketik Search `PT Mandiri Jaya`, tekan Enter
2. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
3. Klik `[Remove]` pada "CV Mitra Mandiri"
4. Verifikasi field `[Group]` diganti `Select Group*`
5. Verifikasi callout "This client has no partner and requires a group to be selected manually."
6. Verifikasi `[Confirm]` disabled
7. Buka tree `Select Group*` lalu klik node "Cabang Menteng"
8. Verifikasi `[Confirm]` aktif
9. Klik `[✕]` pada header dialog
10. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
11. Klik `[Leave]` pada dialog Unsaved Changes

### TC-AC-ACC-457: Add Partner ketiga pada Client yang sudah punya Anchor tidak memunculkan pilih Group manual

12. Ketik Search `PT Teknologi Maju`, tekan Enter
13. Klik `[⋯]` pada baris `PT Teknologi Maju` → klik `Change Partner`
14. Klik `[+ Add Partner]` lalu pilih "CV Mitra Mandiri"
15. Verifikasi tidak ada tree-picker `Select Group*`
16. Verifikasi field `[Group]` read-only tetap tampil
17. Klik `[✕]` pada header dialog
18. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
19. Klik `[Leave]` pada dialog Unsaved Changes
20. Verifikasi dialog Change Partner tertutup tanpa menyimpan

### TC-AC-ACC-179: Survivor tidak bisa di-drag dan Partner baru tidak bisa naik di atas survivor

21. Ketik Search `PT Ganti Mitra`, tekan Enter
22. Klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`
23. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
24. Verifikasi baris survivor "CV Mitra Sejati" tanpa drag handle
25. Coba drag baris survivor "CV Mitra Sejati"
26. Coba drag baris Partner baru "CV Mitra Lestari" ke atas survivor
27. Verifikasi urutan list tetap "CV Mitra Sejati" lalu "CV Mitra Lestari" (Partner baru tidak dapat melewati survivor)
28. Klik `[✕]` pada header dialog
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
30. Klik `[Leave]` pada dialog Unsaved Changes

### TC-AC-ACC-985: [Clear Field] mengembalikan list Partner dan Select Group ke kondisi awal dan [Confirm] kembali disabled

31. Ketik Search `PT Mandiri Jaya`, tekan Enter
32. Klik `[⋯]` pada baris `PT Mandiri Jaya` → klik `Change Partner`
33. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
34. Verifikasi list "Current Partners" memuat "CV Mitra Mandiri" (badge `Active`) dan "CV Mitra Lestari" (badge `New`)
35. Verifikasi `[Confirm]` aktif
36. Klik `[Clear Field]`
37. Verifikasi list "Current Partners" hanya memuat "CV Mitra Mandiri" (badge `Active`)
38. Verifikasi baris "CV Mitra Lestari" tidak ada
39. Verifikasi `[Confirm]` disabled
40. Klik `[Remove]` pada baris "CV Mitra Mandiri"
41. Buka tree `Select Group*` lalu klik node "Cabang Menteng"
42. Verifikasi `Select Group*` terisi "Cabang Menteng"
43. Verifikasi `[Confirm]` aktif
44. Klik `[Clear Field]`
45. Verifikasi list "Current Partners" memuat "CV Mitra Mandiri" (badge `Active`)
46. Verifikasi `Select Group*` tidak tampil
47. Verifikasi field `[Group]` read-only tampil kembali dengan callout "Group is inherited from the topmost partner — drag to reorder if you need a different partner to determine the group."
48. Verifikasi `[Confirm]` disabled
49. Klik `[✕]` pada header dialog
50. Verifikasi dialog Change Partner tertutup langsung
51. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (isi dialog Change Partner sebelum Confirm), satu akun, tanpa mengubah data; tiap blok membuka dialog sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Blok yang berakhir dirty ditutup deterministik lewat `[✕]` dan `[Leave]` (S-08); blok TC-AC-ACC-985 yang berakhir bersih ditaruh paling akhir.
- Langkah penghubung (tanpa awalan Verifikasi): `[✕]` dan `[Leave]` penutup dialog dirty di akhir tiap blok TC-AC-ACC-456, 457, dan 179 (TC-AC-ACC-456 menyebut penutupan ini pada Post Condition).
- TC-AC-ACC-179 Expected "Survivor tanpa drag handle; Partner baru tidak dapat melewati survivor" diurutkan menjadi asersi handle sebelum drag, lalu asersi urutan sesudah drag (butir 5 bagian 8b).
- Temuan untuk QA:
  - TC-AC-ACC-179 tidak menyebut cara menutup dialog yang dirty; spec menutupnya lewat `[✕]` lalu `[Leave]` (S-08, S-09). Langkah TC "Buka Change Partner PT Ganti Mitra" tidak menyebut Search; spec memakai Search nama Client (Tabel A3: baris berpaginasi 10).
  - TC-AC-ACC-457 tidak menyebut langkah akhir pada Expected b selain "dialog tertutup tanpa menyimpan"; spec mengikuti langkah 6 TC (`[Leave]`).
