---
id: TC-AC-PF-E2E-005-plan-detail-header-info-plan-dan-badge-archived
title: "Plan Detail: Header, Info Plan, Tab, dan Badge Archived"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-25
  - TC-AC-PF-26
  - TC-AC-PF-27
coverage:
  web: automated
---

# Plan Detail: Header, Info Plan, Tab, dan Badge Archived

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21): default `Starter` (FAMS, Free, v2), `Growth` (FAMS, Paid, v5), default archived `Growth Plus (old)` (FAMS, Paid, v3), custom `Growth Tier` (FAMS, Paid, v20). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Starter`, `Growth`, `Growth Plus (old)`, `Growth Tier`) dipakai karena menentukan asersi judul, versi, dan badge; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-25: Screening Plan Detail default plan Free aktif: header, info plan, dan tab

1. Klik teks `Starter` pada kolom Plan Name sehingga halaman Plan Detail terbuka
2. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
3. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > Default > Active > Detail`
4. Verifikasi Header: baris judul `Starter – v2` dengan Status Badge `Active`
5. Verifikasi Header: di sisi kanan baris judul tampil ikon Download, button `Edit`, dan button `Archive`
6. Verifikasi Header: ikon Changelog tidak tampil di baris judul
7. Verifikasi Header: baris info memuat badge Product `FAMS`, badge Type `Default`, dan badge Pricing Type `Free`
8. Verifikasi Header: Tab `Overview (aktif) | Assigned Clients`
9. Verifikasi Body: Tab Overview menampilkan SectionCard Feature Matrix `Fixed Asset Module`
10. Verifikasi Footer: tidak ada pagination pada Tab Overview

### TC-AC-PF-26: Screening Plan Detail default plan Paid aktif dan custom plan aktif menampilkan Type dan Pricing Type yang sesuai

11. Klik menu Plans & Licensing > Plans & Features di sidebar
12. Klik teks `Growth` pada kolom Plan Name sehingga Plan Detail `Growth` terbuka
13. Verifikasi judul `Growth – v5` dengan Status Badge `Active`
14. Verifikasi baris info memuat badge Product `FAMS`, badge Type `Default`, dan badge Pricing Type `Paid`
15. Klik menu Plans & Licensing > Plans & Features di sidebar
16. Klik tab Custom
17. Klik teks `Growth Tier` pada kolom Plan Name sehingga Plan Detail `Growth Tier` terbuka
18. Verifikasi judul `Growth Tier – v20` dengan Status Badge `Active`
19. Verifikasi baris info memuat badge Product `FAMS`, badge Type `Custom`, dan badge Pricing Type `Paid`
20. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Custom > Active > Detail`

### TC-AC-PF-27: Plan Detail plan archived menampilkan badge Archived dan tanpa tombol Edit dan Archive

21. Klik menu Plans & Licensing > Plans & Features di sidebar
22. Klik sub-tab Archive
23. Klik teks `Growth Plus (old)` pada kolom Plan Name
24. Verifikasi judul `Growth Plus (old) – v3` dengan Status Badge `Archived`
25. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Default > Archive > Detail`
26. Verifikasi ikon Download tampil di baris judul
27. Verifikasi button `Edit` dan button `Archive` tidak ditampilkan (Hidden) di baris judul

## Notes

- Langkah penghubung (S-03): klik menu sidebar pada langkah 11, 15, dan 21 mengembalikan layar ke list Default > Active sebelum membuka Plan Detail berikutnya; klik tab dan sub-tab pada langkah 16 dan 22 mengarahkan layar ke tab yang disyaratkan TC.
- Langkah "Susuri halaman dari atas ke bawah" adalah langkah observasi TC; asersi tiap bagian halaman ditulis sebagai `Verifikasi` terpisah per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-PF-26: langkah 3 TC berbunyi "Kembali ke tab Custom lalu buka Plan Detail `Growth Tier`" tanpa menyebut cara kembali; spec kembali lewat klik menu sidebar (langkah 15) lalu klik tab Custom.
