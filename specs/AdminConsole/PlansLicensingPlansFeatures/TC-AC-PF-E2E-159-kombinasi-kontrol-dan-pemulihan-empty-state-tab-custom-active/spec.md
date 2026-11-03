---
id: TC-AC-PF-E2E-159-kombinasi-kontrol-dan-pemulihan-empty-state-tab-custom-active
title: Kombinasi Kontrol dan Pemulihan Empty State Tab Custom Active
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-408
  - TC-AC-PF-409
coverage:
  web: automated
---

# Kombinasi Kontrol dan Pemulihan Empty State Tab Custom Active

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (FAMS, v2, Clients 12), `Beta Pro` (SAMS, v10, 7), `Growth Tier` (FAMS, v20, 1), `Zeta Max` (SIEM, v3, 0); semuanya Paid.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-408 Kombinasi empat kontrol dan pelepasan simetris

2. Ketik Search `tier`, tekan Enter.
3. Buka Filter Panel, pilih Product `FAMS`, klik `[Apply]`.
4. Klik header `Clients` dua kali (descending).
5. Verifikasi tabel menampilkan `alpha Tier` (12) lalu `Growth Tier` (1) sebelum Search dikosongkan.
6. Klik ikon `x` pada Search, tekan Enter.
7. Verifikasi Filter Product `FAMS` tetap aktif.
8. Verifikasi sort Clients descending tetap aktif (`alpha Tier`, `Growth Tier`).

### TC-AC-PF-409 Pemulihan empty state

9. Ketik Search `tier`, tekan Enter.
10. Buka Filter Panel, ganti Product `FAMS` menjadi `SIEM`, klik `[Apply]` (hasil kosong).
11. Verifikasi Illustration tampil pada tabel.
12. Verifikasi Title "No results found" tampil.
13. Verifikasi Description "Try adjusting your search or filter." tampil.
14. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.
15. Verifikasi tabel pulih menampilkan `alpha Tier` dan `Growth Tier`.
16. Verifikasi Search `tier` masih aktif.
17. Klik ikon `x` pada Search, tekan Enter.
18. Klik header `Clients` satu kali untuk mengembalikan sort ke netral.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 9 menyetel ulang Search `tier` sebagai kondisi awal TC-AC-PF-409; langkah 17 dan 18 memulihkan Search dan sort.
- TC-AC-PF-409 memecah Expected empty state per butir (Illustration, Title, Description); spec mengikuti pemecahan TC (S-01).
- Anchor absence: empty state pada langkah 11 sampai 13 didahului langkah 8 (baris tabel yang sama tampil sebelum filter diganti).
- Jumlah langkah 18: di bawah ambang sekitar 35.
