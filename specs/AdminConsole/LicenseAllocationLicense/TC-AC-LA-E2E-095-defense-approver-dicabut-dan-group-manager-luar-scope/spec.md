---

id: TC-AC-LA-E2E-095-defense-approver-dicabut-dan-group-manager-luar-scope

title: "Defense-in-Depth: Approver yang Wewenangnya Dicabut dan Group Manager di Luar Scope Group"

priority: Critical

caseType: Negative

status: draft

sourceTc:

  - TC-AC-LA-453

  - TC-AC-LA-454

  - TC-AC-LA-479

coverage:

  web: automated

---



# Defense-in-Depth: Approver yang Wewenangnya Dicabut dan Group Manager di Luar Scope Group



## Prerequisites



- Mode: FE+BE.

- Akun aktor pertama: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

- Akun ganti akun (langkah eksplisit; `Fajar Nugroho` dipakai lagi sebagai pengamat Total Control pada langkah 12): Group Manager + Manage allocation `gmAllocLic_automated_{namaCompany}@qwertysystem.net` (`Hadi Setiawan`, Pre-setup #9), password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`.

- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.

- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga. Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.

- Data Pre-setup (hanya dibaca; semua request ditolak sehingga tidak ada perubahan alokasi): PT Sejahtera (#19), hierarki group Region Jawa (#32) tempat `Hadi Setiawan` di-assign (PT Sejahtera berada di luar Region Jawa), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38). Pencabutan wewenang approver `Fajar Nugroho` (TC-AC-LA-453 dan 454) dilakukan akun admin yang disediakan tim FE dan dipulihkan oleh fixture backend yang disediakan tim FE/BE di langkah penghubung dan hook `after` (S-06, pengecualian 2026-10-30).

- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve; bentuk #41) untuk TC-AC-LA-453, 454, 479. Allocation ID dibaca dari hasil seeding.

- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request Approve dan Reject langsung ke server memakai sesi API akun aktor (login API tidak dihitung sebagai sesi web, `suite.md`), membaca status dan Reserve record lewat fixture BE (tanpa mengarang endpoint, S-13).

- State global yang diubah: wewenang approver `Fajar Nugroho`; dipulihkan di langkah 8 dan di hook `after`. Suite berjalan serial (`parallel: false`).



## Test Steps



### TC-AC-LA-453: Approver yang wewenangnya dicabut tidak dapat Approve



1. Cabut wewenang approver `Fajar Nugroho` lewat akun admin hingga tersimpan

2. Kirim request Approve langsung untuk alokasi `Waiting for Approval` milik `Dewi A`

3. Verifikasi respons server menolak dengan respons error generik

4. Verifikasi status alokasi tetap `Waiting for Approval`



### TC-AC-LA-454: Approver yang wewenangnya dicabut tidak dapat Reject



5. Kirim request Reject langsung untuk alokasi `Waiting for Approval` milik `Dewi A`

6. Verifikasi respons server menolak dengan respons error generik

7. Verifikasi status alokasi tetap `Waiting for Approval`

8. Pulihkan wewenang approver `Fajar Nugroho` lewat fixture backend hingga tersimpan



### TC-AC-LA-479: Group Manager di luar scope group Client target tidak dapat Approve



9. Ganti akun: logout `Fajar N`, login sebagai `Hadi Setiawan` dengan `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`

10. Kirim request Approve langsung untuk alokasi Concurrent User PT Sejahtera

11. Verifikasi respons server menolak dengan respons error generik karena aktor bukan Group Manager scope Client target, bukan Total Control, dan bukan Additional Approver

12. Ganti akun: logout `Hadi S`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`

13. Buka Allocation > License Allocation, ketik Search Allocation ID alokasi itu, tekan Enter, lalu buka Allocation Log alokasi itu

14. Verifikasi status tetap `Waiting for Approval`

15. Verifikasi Reserve $150.00 utuh
16. Tutup modal Allocation Log



## Notes



- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.

- K-1: TC kelas a yang Expected-nya respons API tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend.

- Langkah penghubung (S-03): langkah 1 (mencabut wewenang approver lewat akun admin), 8 (memulihkan wewenang), 9 dan 12 (ganti akun; langkah 12 kembali ke `Fajar Nugroho` sebagai Total Control Distributor pengamat karena `Hadi Setiawan` di luar scope tidak melihat baris itu menurut ACLA-LOGIC-03a), 13 (membuka List, Search, dan Allocation Log), 16 (menutup modal Allocation Log, S-09). Asersi request langsung hanya respons server dan state data (8b butir 1).

- Pembagian TC lintas spec: butir c TC-AC-LA-479 (tidak ada entri `Allocation approved` di Allocation Log, dengan anchor dan baseline) ada di spec 094.

- Temuan untuk QA:

  - TC-AC-LA-453 dan 454 tidak menyebut akun admin dan mekanisme pencabutan wewenang approver; disediakan tim FE.

  - TC-AC-LA-479 Precondition menyebut `Hadi Setiawan` di-assign pada Region Jawa (#32) sedangkan PT Sejahtera di luar Region Jawa; kedudukan PT Sejahtera di luar scope dijamin Pre-setup.

  - TC-AC-LA-479 Expected b dan c (status tetap `Waiting for Approval`, Reserve utuh) tidak menyebut akun pengamat; `Hadi Setiawan` di luar scope tidak dapat melihat baris PT Sejahtera, sehingga spec mengamati sebagai Total Control Distributor `Fajar Nugroho` (usulan: TC menyebut Total Control sebagai pengamat).

  - TC-AC-LA-453, 454, 479 menyebut "respons error generik" tanpa status HTTP; spec mengasersi penolakan tanpa kode.

