---
id: TC-GS-BRAND-E2E-008-guided-tooltip-flag-seen-dan-dismiss
title: "Flag Seen dan Dismiss Guided Tooltip Tab Brand"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-20
  - TC-GS-BRAND-21
  - TC-GS-BRAND-23
  - TC-GS-BRAND-24
coverage:
  web: automated
---

# Flag Seen dan Dismiss Guided Tooltip Tab Brand

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data: memakai data Pre-setup Client A (data environment tetap); spec tidak membuat data.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-brand` sehingga flag direset ke "belum ada" lewat API (hapus flag pada preferensi pengguna) sebelum tiap TC (langkah reset eksplisit). Hook `before` mencatat nilai awal flag; hook `after` memulihkan nilai awal walau spec gagal di tengah.
- Kemampuan teknis: mengubah lebar viewport saat walkthrough berjalan (TC-GS-BRAND-23); hook `after` memulihkan viewport ke ukuran awal. Membaca nilai flag lewat API (untuk Post Condition TC-GS-BRAND-20).
- State global yang diubah: flag Guided Tooltip dan viewport (dipulihkan seperti di atas).

## Test Steps

### TC-GS-BRAND-20: Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelah Skip

1. Hapus flag `guided_tooltip_seen_gs-brand` lewat API sehingga flag belum ada
2. Buka Global Settings > Master Reference > Brand
3. Verifikasi walkthrough muncul otomatis di Step 1
4. Klik [Skip]
5. Verifikasi [Skip] menutup walkthrough
6. Verifikasi flag `guided_tooltip_seen_gs-brand` = true (baca lewat API)
7. Muat ulang halaman
8. Verifikasi walkthrough tidak muncul setelah muat ulang

### TC-GS-BRAND-21: Klik overlay gelap menutup walkthrough dan menyimpan flag seen

9. Hapus flag `guided_tooltip_seen_gs-brand` lewat API sehingga flag belum ada
10. Buka Tab Brand (muat ulang Global Settings > Master Reference) → walkthrough tampil
11. Klik overlay gelap
12. Verifikasi walkthrough tertutup
13. Muat ulang halaman
14. Verifikasi walkthrough tidak muncul lagi setelah muat ulang

### TC-GS-BRAND-23: Resize viewport di tengah walkthrough menutupnya tanpa menyimpan flag

15. Hapus flag `guided_tooltip_seen_gs-brand` lewat API sehingga flag belum ada
16. Buka Tab Brand (muat ulang Global Settings > Master Reference) → walkthrough Step 1 tampil
17. Ubah lebar viewport saat Step 1 tampil
18. Verifikasi walkthrough tertutup
19. Muat ulang halaman
20. Verifikasi walkthrough muncul lagi setelah muat ulang
21. Kembalikan lebar viewport ke ukuran awal

### TC-GS-BRAND-24: Navigasi ke halaman lain di tengah walkthrough tidak menyimpan flag

22. Hapus flag `guided_tooltip_seen_gs-brand` lewat API sehingga flag belum ada
23. Buka Tab Brand (muat ulang Global Settings > Master Reference) hingga walkthrough Step 1 tampil
24. Klik sidebar Global Settings > Activity Log
25. Verifikasi walkthrough tertutup saat berpindah halaman
26. Kembali ke Tab Brand (sidebar Global Settings > Master Reference)
27. Verifikasi walkthrough muncul lagi dari Step 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. Karena flag tersimpan permanen setelah TC-GS-BRAND-20 dan TC-GS-BRAND-21, spec mereset flag lewat API di awal tiap TC (langkah 1, 9, 15, 22) supaya tiap TC mulai dari kondisi "flag belum ada" yang disyaratkan TC sumber.
- Post Condition TC-GS-BRAND-20 (flag = true) diverifikasi pada langkah 6. Post Condition TC-GS-BRAND-21 tidak dicantumkan di TC sumber; penyimpanan flag dibuktikan dari walkthrough yang tidak muncul lagi setelah muat ulang (langkah 14).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 21 (pulihkan viewport ke ukuran awal setelah TC-GS-BRAND-23; hook `after` menjadi cadangan), serta langkah 1, 9, 15, dan 22 (reset flag lewat API untuk memenuhi precondition "flag belum ada").
- Kasus tombol [?], konten step, dan keyboard diuji di spec `TC-GS-BRAND-E2E-007-guided-tooltip-konten-navigasi-keyboard`.
