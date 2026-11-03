---
id: TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah
title: "Defense-in-Depth: Capability Dicabut, Aktor Dinonaktifkan, dan Client Dipindah Binding"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-450
  - TC-AC-LA-451
  - TC-AC-LA-452
  - TC-AC-LA-455
  - TC-AC-LA-529
  - TC-AC-LA-459
coverage:
  web: automated
---

# Defense-in-Depth: Capability Dicabut, Aktor Dinonaktifkan, dan Client Dipindah Binding

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Sesi API `Dewi Anggraini` dibuka di hook `before` sebelum capability dicabut (login API tidak dihitung sebagai sesi web, `suite.md`).
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19) dengan term FAMS `SUBS-20260101-A1B2C` (binding dipindah pada TC-AC-LA-455 lalu dipulihkan), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38). Perubahan atas akun `Dewi Anggraini` (#4: cabut Manage allocation, nonaktifkan) dan binding PT Sejahtera (#19) dilakukan akun admin yang disediakan tim FE dan dipulihkan ke keadaan awal oleh fixture backend yang disediakan tim FE/BE di langkah penghubung antar blok dan hook `after` (S-06, pengecualian 2026-10-30); efek pada Last Updated dan audit trail akun dan Client dicatat di hook `after`.
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup #41, #42, #48): alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` oleh `Dewi A` (Cost $150.00 di-Reserve) dipakai TC-AC-LA-450, 451, 455, 529; alokasi `Waiting for Approval` kedua Concurrent User +10 oleh `Dewi A` dipakai TC-AC-LA-459; alokasi `Canceled` manual Concurrent User +5 oleh `Dewi A` dipakai TC-AC-LA-452. Semua request ditolak sehingga seed tidak berubah. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request Edit, Cancel, Resubmit, dan Approve langsung ke server memakai sesi API `Dewi Anggraini` (tanpa mengarang endpoint, S-13), membaca status dan jumlah record lewat fixture BE.
- State global yang diubah: Manage allocation `Dewi Anggraini`, status aktif akun, binding PT Sejahtera. Dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-450: Aktor yang role Manage allocation-nya dicabut tidak dapat Edit lagi

1. Cabut Manage allocation `Dewi Anggraini` lewat akun admin hingga tersimpan
2. Kirim request Edit langsung untuk alokasi `Waiting for Approval` seed miliknya
3. Verifikasi respons server menolak karena otorisasi dievaluasi saat aksi dengan respons error generik
4. Verifikasi record seed tidak berubah

### TC-AC-LA-451: Aktor yang role-nya dicabut tidak dapat Cancel

5. Kirim request Cancel langsung untuk alokasi `Waiting for Approval` seed miliknya
6. Verifikasi respons server menolak dengan respons error generik
7. Verifikasi status seed tidak berubah (tetap `Waiting for Approval`)

### TC-AC-LA-452: Aktor yang role-nya dicabut tidak dapat Resubmit

8. Catat jumlah alokasi PT Sejahtera lewat fixture BE sebagai baseline
9. Kirim request Resubmit langsung untuk alokasi `Canceled` seed miliknya
10. Verifikasi respons server menolak dengan respons error generik
11. Verifikasi tidak ada record baru (jumlah alokasi PT Sejahtera sama dengan baseline)
12. Pulihkan Manage allocation `Dewi Anggraini` lewat fixture backend hingga tersimpan

### TC-AC-LA-455: Client dipindah binding, aktor tidak dapat Edit alokasi Client itu

13. Pindahkan binding Client `PT Sejahtera` ke Distributor lain lewat akun admin hingga tersimpan
14. Kirim request Edit langsung untuk alokasi `Waiting for Approval` seed milik `Dewi A`
15. Verifikasi respons server menolak dengan respons error generik karena aktor tidak lagi berwenang atas Client itu
16. Pulihkan binding Client `PT Sejahtera` lewat fixture backend hingga tersimpan

### TC-AC-LA-529: Aktor yang dinonaktifkan tidak dapat Edit

17. Nonaktifkan akun `Dewi Anggraini` di Global Settings > User lewat akun admin hingga tersimpan
18. Kirim request Edit langsung untuk alokasi `Waiting for Approval` seed miliknya memakai sesi API yang dibuka sebelum penonaktifan
19. Verifikasi respons server menolak dengan respons error generik karena otorisasi dievaluasi saat aksi dan aktor tidak lagi berwenang
20. Verifikasi record seed tidak berubah
21. Aktifkan kembali akun `Dewi Anggraini` lewat fixture backend hingga tersimpan

### TC-AC-LA-459: Request Approve langsung dari user yang bukan approver

22. Kirim request Approve langsung untuk alokasi `Waiting for Approval` kedua seed milik `Dewi A` memakai akun yang sama
23. Verifikasi respons server menolak (bukan wewenang approver dan self-approval)
24. Verifikasi status seed kedua tidak berubah (tetap `Waiting for Approval`)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend.
- Langkah penghubung (S-03): langkah 8 (baseline S-12), 12, 16, 21 (memulihkan state Pre-setup lewat fixture backend). Asersi hanya respons server dan state data lewat fixture BE (8b butir 1). Capability TC-AC-LA-450 sampai 452 dicabut sekali pada langkah 1 dan dipulihkan pada langkah 12; blok 450, 451, 452 berbagi kondisi itu.
- Asersi absence (langkah 11) berbaseline (langkah 8) dan beranchor respons server yang sudah diasersi (langkah 10).
- Temuan untuk QA:
  - TC-AC-LA-450, 451, 452, 455, 529 tidak menyebut akun admin dan mekanisme pencabutan Manage allocation, pemindahan binding, dan penonaktifan akun; disediakan tim FE.
  - TC-AC-LA-529 Langkah 2 mengirim request atas nama akun yang sudah dinonaktifkan tanpa menyebut sumber token; spec memakai sesi API yang dibuka sebelum penonaktifan. Perilaku token akun nonaktif tidak ditetapkan TC.
  - TC-AC-LA-450, 451, 455, 529 menyebut "respons error generik" tanpa status HTTP; spec mengasersi penolakan tanpa kode.
  - TC-AC-LA-459 Precondition memakai Pre-setup #42 tanpa menyebut requester dan aktor identik; spec memakai seed oleh `Dewi A` dan akun `Dewi Anggraini` yang sama (self-approval).
