---
id: TC-FA-CAID-E2E-038-pencatatan-log-edit-status-separator-segmen
title: "Pencatatan Log Edit: Status dan Separator"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-236
  - TC-FA-CAID-237
  - TC-FA-CAID-238
coverage:
  web: automated
---

# Pencatatan Log Edit: Status dan Separator

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10), dipulihkan oleh hook `beforeEach` suite. General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Master Switch dan Separator konfigurasi Company Alpha berubah. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-236: Log Edit Status saat Toggle ON ke OFF

1. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log, dan Activity Log
2. Geser Master Switch ke OFF
3. Klik `[Disable]`
4. Tunggu aksi selesai: dialog konfirmasi tertutup dan Master Switch berada pada posisi OFF
5. Buka Modal Changelog: Custom Asset ID
6. Verifikasi entri baru (jumlah entri bertambah satu dibanding baseline) Action `Edit`, Field `Status`, Old Value `Active`, New Value `Inactive`
7. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
8. Verifikasi entri baru (jumlah entri bertambah satu dibanding baseline) Object `Custom Asset ID`, Name `—`, Action `Edit`, Field `Status`, Old Value `Active`, New Value `Inactive`
9. Verifikasi System Log tidak memiliki kolom Modified By
10. Buka Fixed Asset > Activity Log > tab User Action
11. Verifikasi entri baru (jumlah entri bertambah satu dibanding baseline) Action `Edit`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Sarah J`

### TC-FA-CAID-237: Log Edit Status saat Toggle OFF ke ON

12. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log, dan Activity Log
13. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu geser Master Switch ke ON
14. Tunggu aksi selesai: Master Switch berada pada posisi ON dan tidak lagi terkunci
15. Buka Modal Changelog: Custom Asset ID
16. Verifikasi entri baru (jumlah entri bertambah satu dibanding baseline) Action `Edit`, Field `Status`, Old Value `Inactive`, New Value `Active`
17. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
18. Verifikasi entri baru (jumlah entri bertambah satu dibanding baseline) Object `Custom Asset ID`, Name `—`, Action `Edit`, Field `Status`, Old Value `Inactive`, New Value `Active`
19. Verifikasi System Log tidak memiliki kolom Modified By
20. Buka Fixed Asset > Activity Log > tab User Action
21. Verifikasi entri baru (jumlah entri bertambah satu dibanding baseline) Action `Edit`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Sarah J`

### TC-FA-CAID-238: Log Edit Separator memakai nama opsi

22. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log, dan Activity Log
23. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu pilih Separator `- (Dash)`
24. Klik `[Save]`
25. Tunggu aksi selesai: tombol `[Save]` kembali disabled
26. Buka Modal Changelog: Custom Asset ID
27. Verifikasi entri baru Action `Edit`, Field `Separator`, Old Value `Slash`, New Value `Dash`
28. Verifikasi Changelog bertambah tepat satu entri dibanding baseline
29. Verifikasi tidak ada baris Status atau Segments Formula baru di Changelog
30. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
31. Verifikasi entri baru Object `Custom Asset ID`, Name `—`, Action `Edit`, Field `Separator`, Old Value `Slash`, New Value `Dash`
32. Verifikasi System Log tidak memiliki kolom Modified By
33. Buka Fixed Asset > Activity Log > tab User Action
34. Verifikasi entri baru Action `Edit`, Field `Separator`, Old Value `Slash`, New Value `Dash`, Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1, 12, dan 22 (baseline jumlah entri, S-12), langkah 13 dan 23 (membuka tab Custom Asset ID bersama aksi), langkah 4, 14, dan 25 (tunggu aksi selesai sebelum membuka Modal Changelog, bagian 8b butir 8), serta membuka Modal Changelog, System Log, dan Activity Log.
- Urutan TC mengikuti nomor TC: TC-FA-CAID-237 berprecondition Master Switch OFF sehingga memakai state hasil TC-FA-CAID-236 (Pre-setup TC: konfigurasi tersimpan dengan Master Switch OFF).
- Langkah 6, 8, dan seterusnya yang memuat "jumlah entri bertambah satu dibanding baseline" memenuhi S-12 dengan baseline jumlah entri; entri baru dicari lewat jumlah, bukan posisi teratas.
- Langkah 9, 19, dan 32 memisahkan klausa "tanpa kolom Modified By" dari baris entri System Log (S-01).
- Segmen yang dicentang diuji di spec 039; judul spec ini hanya Status dan Separator.
- Pembagian TC lintas spec: TC-FA-CAID-233 sampai 235 ada di spec 037, TC-FA-CAID-239 sampai 242 di spec 039, TC-FA-CAID-243 sampai 245 di spec 040.
- Temuan untuk QA:
  - TC-FA-CAID-238 Expected d ("Tidak ada baris Status atau Segments Formula baru") tidak menyebut surface; spec mengasersinya pada Modal Changelog dengan selisih jumlah entri.
  - Post Condition TC-FA-CAID-236 sampai 238 tidak diasersi karena TC tidak memberi langkah observasinya.
