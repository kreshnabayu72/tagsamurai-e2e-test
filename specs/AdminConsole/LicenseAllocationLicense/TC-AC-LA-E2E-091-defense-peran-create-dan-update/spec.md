---
id: TC-AC-LA-E2E-091-defense-peran-create-dan-update
title: "Defense-in-Depth: Penolakan Server untuk Peran Create Saja dan Update Saja"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-75
  - TC-AC-LA-76
  - TC-AC-LA-77
coverage:
  web: automated
---

# Defense-in-Depth: Penolakan Server untuk Peran Create Saja dan Update Saja

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Read+Update `updateOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Yuni Lestari`, Pre-setup #6), password `Spectra.env.AC_LA_DIST_UPDATE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Distributor Create+Read `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`, Pre-setup #5), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Sejahtera (#19), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): alokasi `Canceled` manual Concurrent User +5 milik `Dewi A` (bentuk #48) untuk TC-AC-LA-75; alokasi `Waiting for Approval` Concurrent User +5 milik `Dewi A` (bentuk #41) untuk TC-AC-LA-77; alokasi `Waiting for Approval` Concurrent User +2 ke `SUBS-20260101-A1B2C` PT Sejahtera milik `Doni P` (Cost $60.00 di-Reserve, dibuat saat toggle ON; bentuk #57) untuk TC-AC-LA-76. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request submit, Edit, dan Cancel langsung ke server memakai sesi API akun aktor masing-masing (login API tidak dihitung sebagai sesi web, `suite.md`), membaca jumlah dan status record lewat fixture BE (tanpa mengarang endpoint, S-13).
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah alokasi PT Sejahtera lewat fixture BE sebagai baseline

### TC-AC-LA-75: Read+Update tanpa Create tidak dapat Allocate dan tidak melihat Resubmit

2. Periksa toolbar tab Current
3. Verifikasi `[+ Allocation]` Hidden (anchor: Table Tools tampil di toolbar yang sama)
4. Klik tab `History` dan buka menu `⋯` baris Canceled milik `Dewi A`
5. Verifikasi menu `⋯` memuat `Allocation Log` (anchor)
6. Verifikasi row action `Resubmit` Hidden pada baris Canceled
7. Kirim request submit alokasi langsung ke server dengan akun ini
8. Verifikasi respons server menolak dengan penolakan akses (forbidden)
9. Verifikasi tidak ada record dibuat (jumlah alokasi PT Sejahtera sama dengan baseline)

### TC-AC-LA-77: Update menolak Edit dan Cancel pada record milik orang lain

10. Klik tab `Current` dan buka menu `⋯` pada baris `Waiting for Approval` milik `Dewi A`
11. Verifikasi menu `⋯` hanya berisi `Allocation Log`
12. Kirim request Edit langsung ke server untuk record itu
13. Verifikasi respons server menolak (bukan requester original)
14. Kirim request Cancel langsung ke server untuk record itu
15. Verifikasi respons server menolak (bukan requester original)
16. Verifikasi status record milik `Dewi A` tidak berubah

### TC-AC-LA-76: Create+Read tanpa Update tidak melihat Edit dan Cancel dan ditolak server

17. Ganti akun: logout `Yuni L`, login sebagai `Doni Prasetyo` dengan `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`
18. Buka menu `⋯` pada baris `Waiting for Approval` milik sendiri
19. Verifikasi menu `⋯` hanya berisi `Allocation Log`
20. Kirim request Edit langsung ke server dengan akun ini
21. Verifikasi respons server menolak dengan penolakan akses
22. Kirim request Cancel langsung ke server dengan akun ini
23. Verifikasi respons server menolak dengan penolakan akses
24. Verifikasi status alokasi milik `Doni P` tetap `Waiting for Approval`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor agar semua TC akun Yuni berurutan sebelum satu kali ganti akun ke Doni.
- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend. TC-AC-LA-75, 76, 77 juga memuat bagian UI (visibilitas row action dan tombol) yang diasersi di browser.
- Langkah penghubung (S-03): langkah 1 (baseline S-12), 4 dan 10 (membuka tab dan menu, R-16 tidak diperlukan karena baris dikenali dari seed), 17 (ganti akun). Asersi request langsung hanya respons server dan state data (8b butir 1).
- Asersi absence `Hidden` (langkah 3, 6) beranchor Table Tools dan menu `⋯` yang tampil (8b butir 2); langkah 9 berbaseline.
- Temuan untuk QA:
  - TC-AC-LA-75, 76, 77 menyebut "penolakan akses (forbidden)" tanpa status HTTP; spec mengasersi penolakan tanpa kode.
  - TC-AC-LA-77 Langkah 2 mengirim Edit dan Cancel dalam satu langkah; spec memecahnya menjadi dua request dengan Verifikasi masing-masing.
  - TC-AC-LA-75 Precondition tidak menyebut Allocation ID seed Canceled yang dituju request submit; request submit adalah alokasi baru, bukan Resubmit.
