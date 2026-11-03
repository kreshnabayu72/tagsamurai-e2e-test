---
id: TC-AC-PF-E2E-011-isolasi-state-halaman-dan-filter-antar-sub-tab-active-dan-archive-tab-default
title: "Isolasi State Halaman dan Filter antar Sub-tab Active dan Archive Tab Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-708
  - TC-AC-PF-709
coverage:
  web: automated
---

# Isolasi State Halaman dan Filter antar Sub-tab Active dan Archive Tab Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data (hook `before`): Dataset Plan Z (Pre-setup #38): 12 default plan aktif bernomor urut 01 sampai 12 dengan nama lengkap seperti pada langkah (FAMS: 01 Free, 02 sampai 04 Paid; SAMS: 05 Free, 06 sampai 08 Paid; SIEM: 09 Free, 10 sampai 12 Paid; total Default Active N = 12, 3 di antaranya Free) dan Dataset Plan AR (Pre-setup #48): 12 default plan FAMS Paid archived tidak pernah dipakai `Arsip Default 01` sampai `Arsip Default 12` (total Default Archive N = 12). Slot Free dan Paid per Product terbatas sehingga Dataset Plan Z menggantikan default plan Dataset Plan A selama spec ini berjalan; fixture BE (disediakan tim FE/BE) menyiapkannya di hook `before` dan memulihkan baseline di hook `after`. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (nama plan Dataset Plan Z pada langkah dan `Arsip Default 01` sampai `Arsip Default 12`) dipakai karena menentukan asersi urutan, jumlah, dan teks; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (penggantian dan pemulihan default plan) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-708: State halaman tidak dibagi antar sub-tab Active dan Archive tab Default

1. Pindah ke halaman 2 pada sub-tab Active
2. Klik sub-tab Archive
3. Verifikasi sub-tab Archive berada di halaman 1 dengan teks `Showing 1–10 of 12 entries`
4. Klik sub-tab Active
5. Verifikasi halaman 2 masih aktif di sub-tab Active dengan teks `Showing 11–12 of 12 entries`

### TC-AC-PF-709: Filter yang di-Apply tidak dibagi antar sub-tab Active dan Archive tab Default

6. Klik menu Plans & Licensing > Plans & Features di sidebar
7. Buka Filter Panel, pilih Pricing Type `Free`, klik `[Apply]`
8. Verifikasi sub-tab Active menampilkan tiga baris: `Rencana 01`, `Rencana 05`, `Rencana 09`
9. Klik sub-tab Archive
10. Verifikasi sub-tab Archive tidak tersaring dengan teks `Showing 1–10 of 12 entries`
11. Verifikasi ikon Filter sub-tab Archive tanpa badge titik
12. Klik sub-tab Active
13. Verifikasi filter Pricing Type `Free` masih ter-Apply di sub-tab Active dengan tiga baris yang sama: `Rencana 01`, `Rencana 05`, `Rencana 09`
14. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 6 (klik menu sidebar) mereset state list sebelum TC-AC-PF-709 (S-09); langkah 14 mengosongkan Filter Pricing Type `Free` agar state list tidak terbawa ke hook `after`.
- Temuan untuk QA:
  - Dataset Plan Z (12 default plan aktif dengan 1 Free dan 3 Paid per Product) tidak dapat hidup berdampingan dengan Dataset Plan A pada Product FAMS (slot Free 1 dan Paid 3); TC-AC-PF-708 dan TC-AC-PF-709 menyebut hanya Dataset Plan Z dan Dataset Plan AR, sehingga spec menggantikan Dataset Plan A selama berjalan.
