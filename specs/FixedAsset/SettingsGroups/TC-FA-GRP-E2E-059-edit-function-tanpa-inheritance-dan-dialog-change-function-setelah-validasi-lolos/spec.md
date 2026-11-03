---
id: TC-FA-GRP-E2E-059-edit-function-tanpa-inheritance-dan-dialog-change-function-setelah-validasi-lolos
title: "Edit Function Tanpa Inheritance (Parent Ber-Child) dan Dialog Change Function Hanya Muncul Setelah Validasi Form Lolos"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-979
  - TC-FA-GRP-1025
coverage:
  web: automated
---

# Edit Function Tanpa Inheritance (Parent Ber-Child) dan Dialog Change Function Hanya Muncul Setelah Validasi Form Lolos

## Prerequisites

- Mode: FE+BE (backend nyata; Edit Function menulis data dan hasilnya dibaca di sidebar, tabel, dan badge).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-059` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-979: node `FN Assign {runId}-059` (level 1, Function Assignable; Pre-setup tambahan "FN Assign"). TC-FA-GRP-1025: `Func Parent {runId}-059` (level 1, Function None) dengan satu child `Func Child {runId}-059` (Function None); Pre-setup tambahan "Func Parent > Func Child". Semua di-seed lewat API di hook `before`.
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-059`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-979: Dialog Change Function hanya muncul setelah validasi form lolos

1. Ketik Search `FN Assign {runId}-059`, tekan Enter, buka elipsis (⋯) baris `FN Assign {runId}-059`, klik Edit, kosongkan Group Name, pilih Function None, lalu klik [Save]
2. Verifikasi inline error `Group name must not be empty` di bawah Group Name
3. Verifikasi Dialog Change Function tidak muncul
4. Verifikasi popup tetap terbuka
5. Isi kembali Group Name `FN Assign {runId}-059`, lalu klik [Save]
6. Verifikasi Dialog Change Function (D-01) muncul dengan bullet `FN Assign {runId}-059`
7. Klik [Save] pada dialog
8. Verifikasi submit dijalankan dengan toast sukses `Success, group has been updated.`

### TC-FA-GRP-1025: Edit Function tanpa inheritance

9. Ganti isi kotak Search dengan `Func Parent {runId}-059`, tekan Enter
10. Buka elipsis (⋯) baris `Func Parent {runId}-059`, klik Edit, pilih Function Assignable, lalu klik [Save]
11. Verifikasi Func Parent yang sudah punya child tersimpan sebagai Assignable dengan toast `Success, group has been updated.` tanpa guard container atau leaf
12. Klik `(←)` pada kotak Search
13. Klik `Func Parent {runId}-059` di sidebar
14. Verifikasi Func Child `Func Child {runId}-059` tetap ber-Function None (`—`), tidak mewarisi Function parent
15. Ketik Search `Func Child {runId}-059`, tekan Enter
16. Buka elipsis (⋯) baris `Func Child {runId}-059`, klik Edit, pilih Function Disposal Group, lalu klik [Save]
17. Verifikasi Func Child tersimpan sebagai Disposal Group dengan toast `Success, group has been updated.`
18. Klik `(←)` pada kotak Search
19. Klik All Groups
20. Ketik Search `Func Parent {runId}-059`, tekan Enter
21. Verifikasi Func Parent tetap Assignable (perubahan child tidak naik ke parent)

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah Search pada TC-FA-GRP-979 dan TC-FA-GRP-1025 mencari baris target (R-16); langkah "Ganti isi kotak Search" pada TC-FA-GRP-1025 adalah langkah penghubung (S-03). Langkah 15 dan langkah 20 (Ketik Search) mencari baris Func Child dan Func Parent karena client memiliki lebih dari 10 node level 1 dengan page size 10 dan isi kotak Search tidak diandalkan terbawa saat konteks sidebar berganti; langkah 12 dan langkah 18 (Klik `(←)` pada kotak Search) menutup Search sebelum konteks sidebar berganti, sehingga kotak Search kosong saat langkah 15 dan 20 mengetik.
- Temuan untuk QA:
  - TC-FA-GRP-979 Expected b menyebut "Dialog Change Function (D-01)" tanpa teks Body; spec hanya mengasersi dialog muncul dengan bullet nama node.
  - TC-FA-GRP-1025 langkah 5 menyebut "amati badge Function Func Parent" di All Groups; badge dibaca pada baris Func Parent di tabel All Groups.

