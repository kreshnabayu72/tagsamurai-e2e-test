---
id: TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit
title: "Activate Trial: Ceiling dan Input Digit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-187
  - TC-AC-CS-188
  - TC-AC-CS-211
  - TC-AC-CS-572
  - TC-AC-CS-192
coverage:
  web: automated
---

# Activate Trial: Ceiling dan Input Digit

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: Ceiling Trial `Max Trial Duration` 60 day(s), `Max Trial Asset Quota` 200 assets, `Max Trial Concurrent User Quota` 50 users (#25).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-049` (binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial; padanan Pre-setup #48).
- Data Dinamis: Trial FAMS yang dibuat TC-AC-CS-188 pada Client seed `Client Tanpa Subscription+{runId}-049` adalah satu-satunya perubahan data, dan ikut dihapus bersama Client seed di hook `after`. Ceiling Trial tidak diubah spec ini.
- Kemampuan teknis (disediakan tim FE/BE): membaca Detail baris trial (Duration, Asset Quota, Concurrent User Quota).
- Form Activate Trial dibuka sekali untuk blok validasi (TC-AC-CS-187, 211, 572, 192) dan dikosongkan dengan `[Clear Field]` di antara kasus.

## Test Steps

### TC-AC-CS-187: Nilai di atas ceiling ditolak real-time per field

1. Klik `[+ Activate Trial]`
2. Pilih Product `FAMS`
3. Isi Trial Duration `61`
4. Verifikasi error inline "Trial duration cannot exceed 60 days" pada Trial Duration
5. Isi Trial Asset Quota `201`
6. Verifikasi error inline "Trial asset quota cannot exceed 200" pada Trial Asset Quota
7. Isi Trial Concurrent User Quota `51`
8. Verifikasi error inline "Trial concurrent user quota cannot exceed 50" pada Trial Concurrent User Quota
9. Verifikasi `[Submit]` Disabled selama ada error real-time

### TC-AC-CS-211: Ceiling berlaku juga bagi Principal tanpa exemption

10. Klik `[Clear Field]`
11. Pilih Product `FAMS`
12. Isi Trial Duration `61` sebagai Principal
13. Verifikasi error "Trial duration cannot exceed 60 days" tampil untuk Principal
14. Verifikasi `[Submit]` Disabled

### TC-AC-CS-572: Field kuota dan durasi Trial hanya menerima digit

15. Klik `[Clear Field]`
16. Pilih Product `FAMS`
17. Ketik `abc` pada Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota satu per satu
18. Verifikasi huruf tidak masuk ke Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota
19. Ketik `1.5` pada Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota satu per satu
20. Verifikasi nilai desimal tidak diterima pada ketiga field sehingga isian tetap bilangan bulat
21. Ganti Product ke `SIEM`
22. Ketik `abc` pada Trial Log Source Quota
23. Verifikasi huruf tidak masuk ke Trial Log Source Quota
24. Ketik `1.5` pada Trial Log Source Quota
25. Verifikasi nilai desimal tidak diterima pada Trial Log Source Quota sehingga isian tetap bilangan bulat

### TC-AC-CS-192: Log Source Quota di luar rentang ditolak untuk SIEM

26. Isi Trial Log Source Quota `10000`
27. Verifikasi nilai `10000` memicu "Trial log source quota must be between 1 and 9999"
28. Isi Trial Log Source Quota `0`
29. Verifikasi nilai `0` memicu "Trial log source quota must be between 1 and 9999"
30. Verifikasi `[Submit]` Disabled

### TC-AC-CS-188: Nilai tepat di ceiling diterima

31. Klik `[Clear Field]`
32. Pilih Client `Client Tanpa Subscription+{runId}-049`, Product `FAMS`, Plan `Growth`, isi Trial Duration `60`, Trial Asset Quota `200`, Trial Concurrent User Quota `50`
33. Verifikasi tidak ada error V-20 pada Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota
34. Klik `[Submit]`
35. Tunggu aksi selesai (dialog/modal tertutup)
36. Ketik Search `Client Tanpa Subscription+{runId}-049`, tekan Enter
37. Buka Detail baris trial FAMS
38. Verifikasi Trial Active dibuat dengan Duration 60 hari, Asset Quota 200, dan Concurrent User Quota 50

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-188 (aksi sukses yang menutup form) ditaruh paling akhir supaya semua kasus validasi memakai satu pembukaan form dengan `[Clear Field]` di antara kasus (R-12, bagian 3 prinsip 13).
- Langkah penghubung (S-03): `Tunggu aksi selesai` setelah `[Submit]` sebelum Search (8b.8); `[Clear Field]` antar kasus; Search untuk menemukan baris trial target (R-16).
- TC-AC-CS-572 menyebut empat field: Expected a dan b diasersi per fase (tiga field FAMS lalu Trial Log Source Quota SIEM) karena nilai field berikutnya menimpa isian fase sebelumnya.
- Alasan melewati sekitar 35 langkah: semua blok satu topik (validasi dan batas Activate Trial) pada satu form dan satu dataset, tanpa kelas harness lain; memecahnya hanya menambah login, hook, dan pembukaan form.
- Temuan untuk QA: (1) TC-AC-CS-188 Expected b ("Trial Active dibuat dengan Duration 60 hari, Asset Quota 200, dan Concurrent User Quota 50") tidak menyebut layar pengamatan; spec mengamatinya di Detail trial. (2) TC-AC-CS-187 menyebut `[Submit]` Disabled tetapi Client dan Plan belum terisi; asersi Disabled tidak dapat dibedakan dari akibat field wajib kosong.
