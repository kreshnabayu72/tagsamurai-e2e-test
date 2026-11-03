---
id: TC-AC-LA-E2E-092-defense-approve-reject-oleh-bukan-approver
title: "Defense-in-Depth: Approve dan Reject oleh Bukan Approver, Self-Approval, dan Request ke Alokasi Non-Waiting"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-253
  - TC-AC-LA-482
  - TC-AC-LA-254
  - TC-AC-LA-460
coverage:
  web: automated
---

# Defense-in-Depth: Approve dan Reject oleh Bukan Approver, Self-Approval, dan Request ke Alokasi Non-Waiting

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create+Read dan Additional Approver `createApproverLic_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, Pre-setup #56), password `Spectra.env.AC_LA_CREATE_APPROVER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Distributor Read `readCapLic_automated_{namaCompany}@qwertysystem.net` (`Bayu Aditya`, Pre-setup #7), password `Spectra.env.AC_LA_DIST_READ_PASSWORD`; Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan): PT Sejahtera (#19), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): alokasi `Waiting for Approval` Concurrent User +2 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Eko S` (Cost $60.00 di-Reserve; bentuk #65) untuk TC-AC-LA-253 dan 482; alokasi `Waiting for Approval` Concurrent User +5 oleh `Dewi A` (Cost $150.00 di-Reserve; bentuk #41) untuk TC-AC-LA-254; alokasi `Active` Concurrent User +10 Bengkel Cahaya Motor oleh `Dewi A` (bentuk #47) untuk TC-AC-LA-460. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request Approve dan Reject langsung ke server memakai sesi API akun aktor masing-masing (login API tidak dihitung sebagai sesi web, `suite.md`), membaca status dan Reserve record lewat fixture BE (tanpa mengarang endpoint, S-13).
- State global yang diubah: tidak ada (semua request ditolak). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-253: Requester tidak dapat menyetujui alokasinya sendiri

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi milik `Eko S` sendiri
3. Kirim request Approve langsung untuk alokasi itu
4. Verifikasi respons server menolak (self-approval guard)
5. Verifikasi status alokasi tidak berubah

### TC-AC-LA-482: Requester tidak dapat me-Reject alokasinya sendiri lewat request langsung

6. Kirim request Reject langsung untuk alokasi milik sendiri dengan Rejection Reason `Tidak sesuai`
7. Verifikasi respons server menolak oleh self-approval guard (requester tidak boleh memutus permintaannya sendiri)
8. Buka Allocation Log alokasi itu
9. Verifikasi status tetap `Waiting for Approval`
10. Verifikasi Reserve $60.00 utuh

### TC-AC-LA-254: Approve atau Reject oleh aktor di luar Group Manager, Total Control, dan Additional Approver

11. Ganti akun: logout `Eko S`, login sebagai `Bayu Aditya` dengan `Spectra.env.AC_LA_DIST_READ_PASSWORD`
12. Kirim request Approve langsung untuk alokasi `Waiting for Approval` milik `Dewi A` dengan akun Read
13. Verifikasi respons server menolak dengan respons error generik
14. Kirim request Reject langsung untuk alokasi yang sama dengan akun Read
15. Verifikasi respons server menolak dengan respons error generik
16. Verifikasi status alokasi tidak berubah

### TC-AC-LA-460: Request Approve ke alokasi yang bukan Waiting for Approval ditolak

17. Ganti akun: logout `Bayu A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`
18. Kirim request Approve langsung untuk record `Active`
19. Verifikasi respons server menolak (status bukan Waiting for Approval)
20. Verifikasi record `Active` tidak berubah

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengikuti kebutuhan satu akun berurutan sebelum ganti akun (253, 482, 254, 460). TC-AC-LA-453, 454, dan 479 ada di spec 095 (pencabutan wewenang approver mengubah state global). 
- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend.
- Pembagian TC lintas spec: butir c TC-AC-LA-482 (tidak ada entri `Allocation rejected` di Allocation Log, dengan anchor dan baseline) ada di spec 094.
- Langkah penghubung (S-03): langkah 1 dan 2 (membuka Approvals dan Review sebagai bagian TC-AC-LA-253 Langkah 1), 8 (membuka surface), 11 dan 17 (ganti akun). Asersi request langsung hanya respons server dan state data (8b butir 1).
- Temuan untuk QA:
  - TC-AC-LA-253 Langkah 1 menyebut `[Review]` dibuka lalu "request Approve langsung"; perilaku UI di Review tidak diasersi (8b butir 1).
  - TC-AC-LA-254 Langkah 1 mengirim Approve dan Reject dalam satu langkah; spec memecahnya menjadi dua request dengan Verifikasi masing-masing.
  - TC-AC-LA-253, 482, 254, 460 menyebut "respons error generik" atau penolakan tanpa status HTTP; spec mengasersi penolakan tanpa kode.
