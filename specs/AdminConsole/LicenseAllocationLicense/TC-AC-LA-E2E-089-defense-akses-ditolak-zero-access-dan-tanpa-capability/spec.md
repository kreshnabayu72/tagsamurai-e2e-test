---
id: TC-AC-LA-E2E-089-defense-akses-ditolak-zero-access-dan-tanpa-capability
title: "Defense-in-Depth: Akses Ditolak untuk Zero Access dan Aktor Tanpa Capability"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-444
  - TC-AC-LA-445
  - TC-AC-LA-98
  - TC-AC-LA-458
coverage:
  web: automated
---

# Defense-in-Depth: Akses Ditolak untuk Zero Access dan Aktor Tanpa Capability

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Zero Access `zeroAccessLic_automated_{namaCompany}@qwertysystem.net` (`Wawan Hadi`, Pre-setup #13, Distributor PT Maju Bersama dengan Manage allocation hanya pada group yang tidak memuat Client uji), password `Spectra.env.AC_LA_ZERO_ACCESS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Distributor tanpa capability `noCapabilityLic_automated_{namaCompany}@qwertysystem.net` (`Tono Kusuma`, Pre-setup #12), password `Spectra.env.AC_LA_NO_CAP_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Sejahtera (#19) dengan term FAMS `SUBS-20260101-A1B2C`, kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38) dan OFF (#39).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup #41): alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve) di group tanpa izin Wawan Hadi, dipakai TC-AC-LA-445 dan TC-AC-LA-98. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request submit, Cancel, dan membuka Allocation Log langsung ke server memakai sesi API `Wawan Hadi` (login API tidak dihitung sebagai sesi web, `suite.md`), membaca jumlah alokasi dan status record lewat fixture BE (tanpa mengarang endpoint, S-13).
- State global yang diubah: toggle Require Approval for Allocation OFF untuk TC-AC-LA-444 dan ON untuk TC-AC-LA-445 (diatur fixture backend di langkah penghubung 1 dan 4 dan dipulihkan di hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-444: Submit alokasi Zero Access ditolak dengan penolakan akses grup

1. Atur toggle Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend hingga tersimpan, lalu catat jumlah alokasi PT Sejahtera sebagai baseline
2. Kirim request submit langsung untuk Client `PT Sejahtera` pada group tanpa izin memakai sesi API `Wawan Hadi`
3. Verifikasi respons server menolak dengan penolakan akses grup (forbidden) terlepas state UI
4. Verifikasi tidak ada record dibuat (jumlah alokasi PT Sejahtera sama dengan baseline)

### TC-AC-LA-445: Cancel via request langsung pada group Zero Access ditolak

5. Atur toggle Require Approval for Allocation ON (Pre-setup #38) lewat fixture backend hingga tersimpan
6. Kirim request Cancel langsung untuk alokasi `Waiting for Approval` PT Sejahtera seed
7. Verifikasi respons server menolak dengan penolakan akses grup
8. Verifikasi status alokasi seed tidak berubah (tetap `Waiting for Approval`)

### TC-AC-LA-98: Request langsung membuka Allocation Log record di group Zero Access ditolak

9. Kirim request langsung membuka Allocation Log record seed PT Sejahtera
10. Verifikasi respons server menolak dengan penolakan akses grup (forbidden) terlepas state UI
11. Verifikasi tidak ada data log yang dikembalikan

### TC-AC-LA-458: Direct URL tanpa capability, toast 403 dan UI di-refresh

12. Ganti akun: logout `Wawan Hadi`, login sebagai `Tono Kusuma` dengan `Spectra.env.AC_LA_NO_CAP_PASSWORD`, lalu buka dashboard Admin Console
13. Ketik URL `/admin-console/allocation/license` langsung pada address bar
14. Verifikasi toast error "You don't have permission to do this."
15. Verifikasi UI di-refresh agar elemen tak berhak tersembunyi
16. Verifikasi tidak ada redirect ke halaman terpisah

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a yang Expected-nya respons API (TC-AC-LA-444, 445, 98) tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend. TC-AC-LA-458 berpemicu UI dan mengasersi toast.
- Langkah penghubung (S-03): langkah 1 (baseline S-12 dan toggle), 5 (toggle), 12 (ganti akun dan membuka dashboard). Asersi pada langkah 3, 4, 7, 8, 10, 11 hanya respons server dan state data lewat fixture BE (8b butir 1).
- Asersi absence (langkah 4, 11, 16) berbaseline dan beranchor respons server atau toast yang sudah diasersi.
- Temuan untuk QA:
  - TC-AC-LA-444, 445, 98 menyebut "penolakan akses grup (forbidden)" tanpa status HTTP; spec mengasersi penolakan tanpa kode.
  - TC-AC-LA-98 tidak menyebut Target alokasi selain "record PT Sejahtera Pre-setup #41"; spec memakai seed milik spec.
  - TC-AC-LA-458 Expected a ("UI di-refresh agar elemen tak berhak tersembunyi") tidak menyebut elemen yang menjadi bukti refresh; elemen yang diamati disediakan tim FE.
  - TC-AC-LA-458 Precondition menyebut Pre-setup #12 sebagai "Role: tanpa capability" tetapi Expected menyebut "403"; kode status halaman tidak diasersi.
