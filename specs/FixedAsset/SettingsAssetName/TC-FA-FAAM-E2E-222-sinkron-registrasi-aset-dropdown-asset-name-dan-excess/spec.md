---
id: TC-FA-FAAM-E2E-222-sinkron-registrasi-aset-dropdown-asset-name-dan-excess
title: "Sinkron Registrasi Aset: Dropdown Asset Name Tanpa Category Locked dan Asset Name Baru dengan Baris Policy Tersemai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-598
  - TC-FA-FAAM-599
coverage:
  web: automated
---

# Sinkron Registrasi Aset: Dropdown Asset Name Tanpa Category Locked dan Asset Name Baru dengan Baris Policy Tersemai

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 12 (`MacBook Pro`, Category internal `Electronics` sehingga Category Locked, Total Asset 15; tidak diubah), No. 10 (`Dell Latitude`, dipakai sebagai opsi pembanding di dropdown), No. 22 (Category `IT Equipment`), No. 23 (Brand `Dell`), No. 24 (UoM `Unit`), No. 25 (Label).
- Data Dinamis: `Sync New Item {runId}-222` (Tabel Data Uji Dinamis No. 4; dibuat lewat UI pada TC-FA-FAAM-599 dengan Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`; nilai field TC tidak menyebutnya, lihat Temuan untuk QA).
- Kemampuan teknis: pembukaan Registrasi Aset (dropdown Asset Name), Fixed Asset > Assets, FAMS > Settings > Asset Transactional Policy, serta Modal Changelog dan Search di dalamnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Sync New Item {runId}-222` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-598 dan 599: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-598: Asset Name Category Locked tidak muncul di dropdown Registrasi Aset

1. Buka Registrasi Aset
2. Buka dropdown Asset Name
3. Verifikasi opsi `Dell Latitude` tampil di dropdown
4. Ketik di kotak dropdown `MacBook Pro`
5. Verifikasi `MacBook Pro` tidak ada di dropdown
6. Buka Fixed Asset > Assets
7. Ketik Search `MacBook Pro`, tekan Enter
8. Verifikasi 15 aset `MacBook Pro` tetap tampil (tidak terdampak)

### TC-FA-FAAM-599: Asset Name baru langsung tersedia di dropdown Registrasi Aset dan baris policy tersemai

9. Buka Fixed Asset > Settings > Asset Master > Asset Name
10. Klik `[+ Asset Name]`
11. Isi Asset Name `Sync New Item {runId}-222`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
12. Klik `[Submit]`
13. Buka Registrasi Aset
14. Buka dropdown Asset Name
15. Ketik di kotak dropdown `Sync New Item {runId}-222`
16. Verifikasi `Sync New Item {runId}-222` ada di dropdown Registrasi Aset
17. Buka settings-asset-transactional-policy
18. Ketik Search `Sync New Item {runId}-222`, tekan Enter
19. Verifikasi baris policy `Sync New Item {runId}-222` dengan nilai default Borrow `On`, Assign `On`, Transfer `On`, Self Service Borrow `Off`
20. Buka Fixed Asset > Settings > Asset Master > Asset Name
21. Klik icon Changelog
22. Ketik Search `Sync New Item {runId}-222`, tekan Enter
23. Verifikasi Changelog hanya memuat satu baris Create untuk `Sync New Item {runId}-222` tanpa entri untuk penyemaian policy
24. Tutup Modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 6, 9, 13, 17, 20 (navigasi), langkah 4, 15 (mengetik di kotak pencarian dropdown), langkah 7, 18 (Search), langkah 21, 22, 24 (membuka, mencari, dan menutup Modal Changelog; S-12, S-14).
- Langkah 5 adalah asersi absence atas opsi dropdown dengan anchor positif langkah 3 (opsi pembanding pada dropdown yang sama; bagian 8b butir 2). Langkah 23 mengasersi jumlah baris Changelog (satu baris Create), bukan absence murni.
- Pembagian TC lintas spec: TC-FA-FAAM-739 dan 740 ada di spec 244; TC-FA-FAAM-675 di spec 243.
- Temuan untuk QA:
  - TC-FA-FAAM-599 tidak menyebut nilai Category, TAG Type, Brand, dan UoM; spec memilih nilai Pre-setup No. 22 sampai 24.
  - TC-FA-FAAM-599 butir c "Tanpa entri Changelog" ambigu (apakah tidak ada entri sama sekali termasuk Create); spec mengikuti TC-FA-FAAM-741 butir c (satu baris Create tanpa entri penyemaian policy).
  - Kuantitas aset `MacBook Pro` (15) berasal dari Pre-setup No. 12; TC-FA-FAAM-598 hanya menyebut "tidak terdampak".
