---
id: TC-AC-SU-E2E-208-modal-changelog-global-role-mencatat-cascade-total-control-dan-read-only
title: "Modal Changelog User > Global Role Mencatat Assign dan Remove via Total Control atau Read Only (Cascade)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-553
  - TC-AC-SU-554
  - TC-AC-SU-555
  - TC-AC-SU-556
coverage:
  web: automated
---

# Modal Changelog User > Global Role Mencatat Assign dan Remove via Total Control atau Read Only (Cascade)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12). Nama unik sehingga entri audit trail user hanya berasal dari spec ini; asersi memakai Action dan Role Name, bukan jumlah entri absolut. Data Pre-setup bersama tidak diubah. Satu user per TC: user blok Remove di-seed langsung bertier sehingga blok Remove tidak bergantung pada blok Assign:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-208A` | `miketan+{runId}-208a@qwertysystem.net` | Activated, tanpa tier, "Manage group" belum aktif (TC-553) |
| U2 | `Mike Tan {runId}-208B` | `miketan+{runId}-208b@qwertysystem.net` | Activated, bertier Total Control, "Manage group" aktif (TC-555) |
| U3 | `Mike Tan {runId}-208C` | `miketan+{runId}-208c@qwertysystem.net` | Activated, tanpa tier, "Manage group" belum aktif (TC-554) |
| U4 | `Mike Tan {runId}-208D` | `miketan+{runId}-208d@qwertysystem.net` | Activated, bertier Read Only, "Manage group" aktif (TC-556) |

- Kemampuan teknis: Fixture BE (seeding user, tier, dan role). Daftar Global Role yang terdampak cascade tier mengikuti katalog Settings > Role & Permission (`Fixture.settingsUser.globalRoles`, kunci fixture baru yang disediakan tim FE). Date baris dibandingkan antar surface pada menit yang sama (resolusi menit). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-553: Assign (via Total Control)
1. Klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu assign U1 ke Total Control
2. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U1 lewat Search nama, klik Tab Role, sub-tab Global Role, lalu klik icon Changelog di toolbar
3. Ubah page size Modal Changelog menjadi 100
4. Verifikasi baris modal: Action `Assign (via Total Control)`, Role Name `Manage group`, Field `Access`, Old Value `—`, New Value `Assigned`
5. Verifikasi tiap Global Role terdampak memiliki tepat 1 baris Action `Assign (via Total Control)` (jumlah sama dengan katalog Global Role), lalu catat Date baris cascade
6. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-208A` pada Popup Changelog: User, tekan Enter
7. Verifikasi Date baris Popup Changelog: User Action `Assign`, Field `Access Level`, New Value `Total Control` sama dengan Date baris cascade (langkah 5)
### TC-AC-SU-555: Remove (via Total Control)
8. Tutup popup, klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu remove U2 dari Total Control
9. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U2 lewat Search nama, klik Tab Role, sub-tab Global Role, lalu klik icon Changelog di toolbar
10. Ubah page size Modal Changelog menjadi 100
11. Verifikasi baris modal: Action `Remove (via Total Control)`, Role Name `Manage group`, Field `Access`, Old Value `Assigned`, New Value `—`
12. Verifikasi tiap Global Role terdampak memiliki tepat 1 baris Action `Remove (via Total Control)`, lalu catat Date baris cascade
13. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-208B` pada Popup Changelog: User, tekan Enter
14. Verifikasi Date baris Popup Changelog: User Action `Remove`, Field `Access Level`, Old Value `Total Control` sama dengan Date baris cascade (langkah 12)
### TC-AC-SU-554: Assign (via Read Only)
15. Tutup popup, klik menu Settings > Role & Permission di sidebar, klik Tab Read Only, lalu assign U3 ke Read Only
16. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U3 lewat Search nama, klik Tab Role, sub-tab Global Role, lalu klik icon Changelog di toolbar
17. Ubah page size Modal Changelog menjadi 100
18. Verifikasi baris modal: Action `Assign (via Read Only)`, Role Name `Manage group`, Field `Access`, Old Value `—`, New Value `Assigned`
19. Verifikasi tiap Global Role terdampak memiliki tepat 1 baris Action `Assign (via Read Only)`, lalu catat Date baris cascade
20. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-208C` pada Popup Changelog: User, tekan Enter
21. Verifikasi Date baris Popup Changelog: User Action `Assign`, Field `Access Level`, New Value `Read Only` sama dengan Date baris cascade (langkah 19)
### TC-AC-SU-556: Remove (via Read Only)
22. Tutup popup, klik menu Settings > Role & Permission di sidebar, klik Tab Read Only, lalu remove U4 dari Read Only
23. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U4 lewat Search nama, klik Tab Role, sub-tab Global Role, lalu klik icon Changelog di toolbar
24. Ubah page size Modal Changelog menjadi 100
25. Verifikasi baris modal: Action `Remove (via Read Only)`, Role Name `Manage group`, Field `Access`, Old Value `Assigned`, New Value `—`
26. Verifikasi tiap Global Role terdampak memiliki tepat 1 baris Action `Remove (via Read Only)`, lalu catat Date baris cascade
27. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-208D` pada Popup Changelog: User, tekan Enter
28. Verifikasi Date baris Popup Changelog: User Action `Remove`, Field `Access Level`, Old Value `Read Only` sama dengan Date baris cascade (langkah 26)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search nama user dan pembukaan Detail (langkah 2 dan langkah serupa, R-16), mengubah page size Modal Changelog menjadi 100 agar semua baris cascade tampil sebelum asersi "tepat 1 baris" (langkah 3, 10, 17, 24; S-14), Search nama user di Popup Changelog: User (langkah 6 dan langkah serupa; nama unik sehingga hanya entri user itu yang tampil), menutup modal dan popup, serta pencatatan Date.
- Urutan blok: TC-553 (U1), TC-555 (U2), TC-554 (U3), TC-556 (U4); dua pasangan Total Control lalu Read Only. Urutan ini mengubah urutan nomor TC (S-10). Tiap blok memakai user sendiri sehingga blok Remove tidak bergantung pada blok Assign. Baris target tiap Verifikasi dicari lewat Action dan Role Name pada Modal Changelog (bukan lewat posisi baris), setelah page size 100 (S-14).
- Pembagian TC lintas spec: TC-550, TC-551, dan TC-552 ada di spec 162. Empat blok di spec ini berpola sama (pemicu satu aksi tier, satu modal, satu padanan di Popup Changelog: User) pada empat user terpisah dan satu aktor; 28 langkah (tidak melewati batas 35).
- Temuan untuk QA:
  - TC-553 sampai TC-556 butir a menyebut "Role Name sesuai role" tanpa menyebut role yang diasersi; spec mengasersi baris `Manage group` dan jumlah baris sama dengan katalog Global Role (10 role menurut precondition TC; `settings-role-permission.md` §2.6).
  - TC-553 sampai TC-556 butir b membandingkan Date baris cascade dengan Popup Changelog: User pada resolusi menit; asersi dapat berbeda satu menit bila aksi melewati pergantian menit.
  - Precondition TC-555 dan TC-556 menyatakan user sudah bertier; spec men-seed user blok Remove langsung bertier Total Control atau Read Only.
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
