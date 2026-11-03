---
id: TC-AC-CS-E2E-050-activate-trial-kuota-kosong-dan-batas-bawah
title: "Activate Trial: Kuota Kosong dan Batas Bawah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-189
  - TC-AC-CS-190
  - TC-AC-CS-191
  - TC-AC-CS-193
coverage:
  web: automated
---

# Activate Trial: Kuota Kosong dan Batas Bawah

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-050` (binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial; padanan Pre-setup #48).
- Data Dinamis: trial FAMS (TC-AC-CS-191) dan trial SIEM (TC-AC-CS-193 tidak disubmit) hanya pada Client seed `Client Tanpa Subscription+{runId}-050`, dihapus bersama Client seed di hook `after`.
- Form Activate Trial dibuka sekali untuk blok validasi dan dikosongkan dengan `[Clear Field]` di antara kasus.

## Test Steps

### TC-AC-CS-189: Kuota atau durasi kosong ditolak real-time

1. Klik `[+ Activate Trial]`
2. Pilih Product `FAMS`
3. Kosongkan Trial Duration
4. Verifikasi error inline "Trial duration must not be empty"
5. Kosongkan Trial Asset Quota
6. Verifikasi error inline "Trial asset quota must not be empty"
7. Kosongkan Trial Concurrent User Quota
8. Verifikasi error inline "Trial concurrent user quota must not be empty"
9. Pilih Product `SIEM`
10. Kosongkan Trial Log Source Quota
11. Verifikasi error inline "Trial log source quota must not be empty"
12. Verifikasi `[Submit]` Disabled selama ada error

### TC-AC-CS-190: Nilai di bawah 1 ditolak real-time

13. Klik `[Clear Field]`
14. Pilih Product `FAMS`
15. Isi Trial Duration `0`
16. Verifikasi error inline "Trial duration must be at least 1 day"
17. Isi Trial Asset Quota `0`
18. Verifikasi error inline "Trial asset quota must be at least 1"
19. Isi Trial Concurrent User Quota `0`
20. Verifikasi error inline "Trial concurrent user quota must be at least 1"
21. Verifikasi `[Submit]` Disabled

### TC-AC-CS-193: Log Source Quota 1 dan 9999 diterima

22. Klik `[Clear Field]`
23. Pilih Client `Client Tanpa Subscription+{runId}-050`, Product `SIEM`, Plan SIEM, isi Trial Duration `30`, Trial Concurrent User Quota `10`, Trial Log Source Quota `9999`
24. Verifikasi tidak ada error pada Trial Log Source Quota untuk nilai `9999`
25. Ubah Trial Log Source Quota menjadi `1`
26. Verifikasi tidak ada error pada Trial Log Source Quota untuk nilai `1`
27. Verifikasi `[Submit]` Enabled
28. Klik `[✕]`
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil
30. Klik `[Leave]`

### TC-AC-CS-191: Nilai batas bawah 1 diterima

31. Klik `[+ Activate Trial]`
32. Pilih Client `Client Tanpa Subscription+{runId}-050`, Product `FAMS`, Plan `Growth`, isi Trial Duration `1`, Trial Asset Quota `1`, Trial Concurrent User Quota `1`
33. Verifikasi tidak ada error pada Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota
34. Klik `[Submit]`
35. Tunggu aksi selesai (dialog/modal tertutup)
36. Ketik Search `Client Tanpa Subscription+{runId}-050`, tekan Enter
37. Buka Detail baris trial FAMS
38. Verifikasi Trial Active dibuat dengan End Date sama dengan Start Date (1 hari, End Date inklusif)

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-191 (aksi sukses) ditaruh paling akhir supaya blok validasi dan kasus tanpa submit memakai satu pembukaan form dan trial FAMS yang dibuat tidak memengaruhi kasus lain.
- Langkah penghubung (S-03): `Tunggu aksi selesai` setelah `[Submit]` sebelum Search (8b.8); `[Clear Field]` antar kasus (R-12); form TC-AC-CS-193 yang berakhir dirty ditutup deterministik dengan `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08, S-09); Search untuk menemukan baris trial target (R-16).
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu topik (validasi dan batas Activate Trial) pada satu form dan satu dataset, tanpa kelas harness lain; memecahnya hanya menambah login, hook, dan pembukaan form.
- Temuan untuk QA: (1) TC-AC-CS-191 Expected b tidak menyebut layar pengamatan Start Date dan End Date; spec mengamatinya di Detail trial. (2) TC-AC-CS-193 tidak submit; asersi hanya state field dan tombol.
