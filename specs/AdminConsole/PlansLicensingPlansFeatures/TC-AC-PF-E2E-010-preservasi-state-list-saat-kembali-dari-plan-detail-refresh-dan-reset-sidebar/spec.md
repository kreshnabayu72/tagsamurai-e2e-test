---
id: TC-AC-PF-E2E-010-preservasi-state-list-saat-kembali-dari-plan-detail-refresh-dan-reset-sidebar
title: "Preservasi State List saat Kembali dari Plan Detail, Refresh, dan Reset Lewat Sidebar (Dataset 120 Custom Plan)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-40
  - TC-AC-PF-41
  - TC-AC-PF-42
  - TC-AC-PF-43
coverage:
  web: automated
---

# Preservasi State List saat Kembali dari Plan Detail, Refresh, dan Reset Lewat Sidebar (Dataset 120 Custom Plan)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data (hook `before`): Dataset Plan B (Pre-setup #22): 120 custom plan Principal `Paket 001` sampai `Paket 120` (FAMS, Paid, v1, Clients 0). Volume 100 baris atau lebih (kelas e); seeding lewat fixture BE yang idempoten, disediakan tim FE/BE. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Paket 001` sampai `Paket 120`) dipakai karena menentukan asersi urutan, jumlah, dan teks; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: kontrol tombol Back browser dan F5; fixture BE (seeding 120 plan dan pemulihan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-40: Kembali dari Plan Detail lewat tombol Back browser mempertahankan Search, Sort, Filter, dan halaman

1. Klik tab Custom
2. Ketik Search `Paket`, tekan Enter
3. Klik header Plan Name dua kali (descending)
4. Terapkan Filter Product `FAMS` (buka Filter Panel, pilih Product `FAMS`, klik `[Apply]`)
5. Pindah ke halaman 2
6. Klik teks Plan Name pada baris pertama
7. Klik tombol Back browser
8. Verifikasi Search `Paket` masih terpasang
9. Verifikasi sort Plan Name descending masih aktif
10. Verifikasi Filter Product `FAMS` ter-Apply
11. Verifikasi halaman 2 aktif

### TC-AC-PF-41: Kembali dari Plan Detail lewat breadcrumb sub-tab mempertahankan state list

12. Klik menu Plans & Licensing > Plans & Features di sidebar
13. Klik tab Custom
14. Ketik Search `Paket`, tekan Enter
15. Pindah ke halaman 2
16. Klik teks Plan Name pada baris pertama untuk membuka Plan Detail
17. Klik segmen `Active` pada breadcrumb
18. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active tampil
19. Verifikasi Search `Paket` masih terpasang
20. Verifikasi halaman 2 aktif

### TC-AC-PF-42: Refresh F5 pada list mempertahankan Search, Sort, Filter, dan halaman pada tab yang sama

21. Klik menu Plans & Licensing > Plans & Features di sidebar
22. Klik tab Custom
23. Ketik Search `Paket`, tekan Enter
24. Terapkan Filter Product `FAMS` (buka Filter Panel, pilih Product `FAMS`, klik `[Apply]`)
25. Pindah ke halaman 2
26. Tekan F5
27. Verifikasi Search `Paket` tetap terpasang
28. Verifikasi Filter Product `FAMS` tetap ter-Apply
29. Verifikasi halaman 2 tetap aktif

### TC-AC-PF-43: Klik ulang menu Plans & Features dari sidebar mereset Search, Sort, Filter, dan halaman ke default

30. Klik menu Plans & Licensing > Plans & Features di sidebar
31. Klik tab Custom
32. Ketik Search `Paket`, tekan Enter, lalu pindah ke halaman 2
33. Klik menu Plans & Licensing > Plans & Features di sidebar
34. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil
35. Verifikasi tidak ada Search yang terpasang
36. Verifikasi tidak ada Filter yang ter-Apply
37. Verifikasi sort default
38. Verifikasi halaman 1 aktif

## Notes

- Langkah penghubung (S-03): klik menu sidebar pada langkah 12, 21, dan 30 mereset state list sebelum TC berikutnya (S-09) dan mengarahkan layar ke list awal; klik tab Custom pada langkah 1, 13, 22, dan 31 mengarahkan layar ke tab yang disyaratkan precondition TC. Langkah 6 dan 16 membuka Plan Detail dari baris pertama sesuai langkah TC.
- Alasan di atas sekitar 35 langkah (38 langkah): keempat blok satu topik (preservasi state list) dan satu kelas harness (kelas e volume data, Dataset Plan B), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected dipecah satu `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-PF-40 dan TC-AC-PF-42: Filter Product `FAMS` pada Dataset Plan B (seluruh plan FAMS) tidak mengubah hasil sehingga asersi "Filter Product `FAMS` ter-Apply" tidak membuktikan penyaringan; spec mengikuti TC.
  - TC-AC-PF-43: Expected menyebut "sort default" tanpa menyebut kolom dan arahnya; spec mengasersi sesuai kalimat TC.
