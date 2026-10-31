---
id: TC-GS-TAG-E2E-049-bulk-delete-dialog-screening-varian-peringatan-dan-cancel
title: "Dialog Bulk Delete: Screening, Varian Peringatan (Waiting for Approval/Retired), Collapse Satu Baris, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-151
  - TC-GS-TAG-152
  - TC-GS-TAG-154
coverage:
  web: automated
---

# Dialog Bulk Delete: Screening, Varian Peringatan (Waiting for Approval/Retired), Collapse Satu Baris, dan Cancel

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini hanya membuka dialog Bulk Delete lalu `Cancel`; tidak ada penghapusan data.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30). Baris yang dipakai: DD-02 `E2801160600002054D8A0002` (Available), DD-04 `AABBCCDDEE80` (Damaged/Missing), DD-03 (Waiting for Approval), DD-08 (Retired). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); seeding idempotent lewat fixture BE memulihkan kondisi awal sebelum spec.
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-151: Dialog Delete TAGs

1. Centang baris DD-02 dan DD-04
2. Pilih `Bulk Action` > `Delete`
3. Verifikasi judul dialog `Delete TAGs`
4. Verifikasi bullet `E2801160600002054D8A0002` dan `AABBCCDDEE80` tampil dalam container scrollable
5. Verifikasi body memuat baris `This will free up license quota.`
6. Verifikasi body memuat baris `For more accurate results, use Delete by Scan.`
7. Verifikasi body memuat kalimat `Are you sure you want to delete them? This action cannot be undone.`
8. Verifikasi footer memuat tombol `Cancel` dan `Delete`
9. Klik `Cancel`
10. Verifikasi dialog tertutup
11. Verifikasi baris DD-02 dan DD-04 tetap tampil di registri (tidak ada baris terhapus)
12. Verifikasi seleksi dan Bulk Action Bar dipertahankan
13. Verifikasi tidak ada toast

### TC-GS-TAG-152: Varian peringatan Dialog 5

14. Klik `(✕)` pada Bulk Action Bar untuk membatalkan seleksi
15. Centang baris DD-03 (Waiting for Approval) dan DD-02
16. Pilih `Bulk Action` > `Delete`
17. Verifikasi dialog memuat baris peringatan `This will free up license quota and pending approval will be canceled.`
18. Klik `Cancel` untuk menutup dialog
19. Klik `(✕)` pada Bulk Action Bar untuk melepas seleksi
20. Centang hanya baris DD-08 (Retired)
21. Pilih `Bulk Action` > `Delete`
22. Verifikasi baris petunjuk `For more accurate results, use Delete by Scan.` tetap tampil
23. Verifikasi dialog tidak memuat baris peringatan
24. Klik `Cancel` untuk menutup dialog

### TC-GS-TAG-154: Bulk Delete satu baris collapse ke dialog single

25. Klik `(✕)` pada Bulk Action Bar untuk melepas seleksi
26. Centang baris DD-02
27. Pilih `Bulk Action` > `Delete`
28. Verifikasi dialog berjudul `Delete TAG` (singular)
29. Verifikasi dialog memuat `Are you sure you want to delete it?`
30. Klik `Cancel` untuk menutup dialog
31. Klik `(✕)` pada Bulk Action Bar untuk melepas seleksi

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 14, 19, 25, 31 (membersihkan seleksi), 18 dan 24 dan 30 (`Cancel` pada dialog yang hanya diamati).
- Asersi tambahan di luar Expected TC (S-03): tidak ada; langkah 10 (dialog tertutup) mengikuti Expected d TC-GS-TAG-151.
- Temuan untuk QA:
  - Q-4: identifier Seed Registri A tetap; kondisi dipulihkan lewat fixture BE sebelum spec.
  - TC-GS-TAG-152 Expected a hanya memuat baris peringatan; TC tidak menyatakan apakah baris `This will free up license quota.` ikut tampil pada seleksi campuran, sehingga tidak diasersi.
  - TC-GS-TAG-154 tidak punya langkah menutup dialog; langkah 30 adalah penghubung.
  - Post Condition semua TC bernilai `-`.
