---
id: TC-AC-ACC-E2E-117-change-partner-remove-anchor-dan-urutan-drag
title: "Change Partner oleh Principal: Remove Anchor Memindahkan Group Otomatis dan Urutan List Menentukan Anchor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-176
  - TC-AC-ACC-599
  - TC-AC-ACC-178
  - TC-AC-ACC-600
coverage:
  web: automated
---

# Change Partner oleh Principal: Remove Anchor Memindahkan Group Otomatis dan Urutan List Menentukan Anchor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): empat replika bersuffix dengan atribut setara fixture asal: `PT Pindah Anchor Uji {runId}-117` (setara C-ISO-3: Active, Anchor CV Mitra Sejati 2026-01-05 + CV Mitra Lestari 2026-02-10, Group Area Jakarta, tanpa subscription); `PT Tiga Mitra {runId}-117` (setara C-ROL-11: Active, relasi CV Mitra Sejati 2026-01-05, CV Mitra Mandiri 2026-02-10, CV Mitra Lestari 2026-03-15, Group Area Jakarta, FAMS Active); `PT Direct Tambah Mitra {runId}-117` (setara C-ISO-5: Active, Direct, Group Cabang Menteng, tanpa subscription); `PT Ubah Mitra 10 {runId}-117` (setara C-ROL-8: Active, satu-satunya Partner CV Mitra Sejati, Group Area Jakarta, tanpa subscription). Relasi lama yang dilepas menjadi `transferred` hanya pada replika. Client C-ISO-3, C-ROL-11, C-ISO-5, dan C-ROL-8 `PT Ubah Mitra 10` literal tidak disentuh.
- Partner pembanding Active: `CV Mitra Sejati`, `CV Mitra Lestari`, `CV Mitra Mandiri` (Group Cabang Bekasi).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-176: Remove Anchor dengan Partner lain tersisa: Group pindah otomatis tanpa pilih manual

1. Ketik Search `PT Pindah Anchor Uji {runId}-117`, tekan Enter
2. Klik `[⋯]` pada baris `PT Pindah Anchor Uji {runId}-117` → klik `Change Partner`
3. Klik `[Remove]` pada "CV Mitra Sejati"
4. Verifikasi field `[Group]` live-update ke Group Partner tersisa
5. Verifikasi tidak ada tree-picker `Select Group*`
6. Klik `[Confirm]`
7. Verifikasi toast sukses "Success, partner has been updated."
8. Verifikasi Managed By baris `PT Pindah Anchor Uji {runId}-117` adalah "CV Mitra Lestari"

### TC-AC-ACC-599: Remove Anchor dari tiga Partner: Anchor pindah ke penetapan tertua berikutnya

9. Ketik Search `PT Tiga Mitra {runId}-117`, tekan Enter
10. Klik `[⋯]` pada baris `PT Tiga Mitra {runId}-117` → klik `Change Partner`
11. Klik `[Remove]` pada "CV Mitra Sejati"
12. Verifikasi field `[Group]` read-only tetap tampil
13. Verifikasi `Select Group*` tidak tampil
14. Klik `[Confirm]`
15. Verifikasi toast sukses "Success, partner has been updated."
16. Verifikasi Managed By baris `PT Tiga Mitra {runId}-117` adalah "CV Mitra Mandiri" diikuti `+1 more`
17. Verifikasi Group baris `PT Tiga Mitra {runId}-117` adalah "Cabang Bekasi"
18. Klik `[⋯]` pada baris `PT Tiga Mitra {runId}-117` → klik `Change Partner`
19. Verifikasi list "Current Partners" memuat "CV Mitra Mandiri" dan "CV Mitra Lestari"
20. Verifikasi list "Current Partners" tidak memuat "CV Mitra Sejati"
21. Klik `[✕]` pada header dialog

### TC-AC-ACC-178: Dua Partner baru tanpa survivor: urutan list menentukan Anchor dan dapat di-drag

22. Ketik Search `PT Direct Tambah Mitra {runId}-117`, tekan Enter
23. Klik `[⋯]` pada baris `PT Direct Tambah Mitra {runId}-117` → klik `Change Partner`
24. Klik `[+ Add Partner]` lalu pilih "CV Mitra Sejati" kemudian "CV Mitra Lestari"
25. Drag "CV Mitra Lestari" ke atas "CV Mitra Sejati"
26. Verifikasi field `[Group]` read-only live-update mengikuti Partner teratas
27. Verifikasi Anchor adalah "CV Mitra Lestari" setelah drag
28. Klik `[Confirm]`
29. Verifikasi Managed By baris `PT Direct Tambah Mitra {runId}-117` adalah "CV Mitra Lestari" diikuti `+1 more`

### TC-AC-ACC-600: Remove Partner lama dan menambah dua Partner baru: urutan list menentukan Anchor

30. Ketik Search `PT Ubah Mitra 10 {runId}-117`, tekan Enter
31. Klik `[⋯]` pada baris `PT Ubah Mitra 10 {runId}-117` → klik `Change Partner`
32. Klik `[Remove]` pada "CV Mitra Sejati"
33. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari" kemudian "CV Mitra Mandiri"
34. Verifikasi kedua Partner baru tampil dengan badge `New`
35. Verifikasi kedua Partner baru memiliki drag handle
36. Drag "CV Mitra Mandiri" ke atas "CV Mitra Lestari"
37. Klik `[Confirm]`
38. Verifikasi toast sukses "Success, partner has been updated."
39. Verifikasi Managed By baris `PT Ubah Mitra 10 {runId}-117` adalah "CV Mitra Mandiri" diikuti `+1 more`
40. Verifikasi Group baris `PT Ubah Mitra 10 {runId}-117` adalah "Cabang Bekasi"

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (penentuan Anchor oleh Remove dan urutan list) dengan satu akun; empat replika Client berbeda milik spec sehingga tiap blok tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): `[✕]` menutup dialog pemeriksaan di TC-AC-ACC-599 (langkah 21; dialog bersih).
- TC-AC-ACC-178 Expected a ("Group read-only live-update mengikuti Partner teratas") ditaruh setelah drag bersama Expected b karena Langkah TC 5 (Lihat Group) berada sesudah Langkah 4 (drag); asersi Anchor sesudah drag mengikuti Expected b.
- Post Condition TC-AC-ACC-176 (relasi "CV Mitra Sejati" `transferred`, Anchor tidak dapat dipulihkan lewat UI), TC-AC-ACC-599, 600, dan 178 (seed ulang fixture): tanpa langkah observasi di TC, tidak diasersi; seed ulang tidak diperlukan karena target adalah replika milik spec yang dibersihkan hook `after`.
- Temuan untuk QA:
  - TC-AC-ACC-176 Expected a menyebut "Group live-update ke Group Partner tersisa" tanpa menyebut nama Group; spec tidak menambahkan nilai Group yang tidak tertulis.
  - TC-AC-ACC-178 Expected tidak menyebut Group akhir (Cabang Menteng atau Group CV Mitra Lestari) di List; spec hanya mengasersi Managed By sesuai Expected c.
