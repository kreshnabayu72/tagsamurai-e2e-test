---
name: Admin Console License Allocation
id: suite-admin-console-license-allocation-license
description: Spec e2e turunan tc-license-allocation-license.md untuk Admin Console > Allocation > License Allocation
executionOrder: 2.0
parallel: false
---

# Suite: Admin Console License Allocation

Suite ini mencakup halaman Allocation > License Allocation: tabel List dengan tab Current dan History (Search, Filter, Sort, Pagination, Setup Column, Download, preservasi state), Modal Allocation Log dan Modal Changelog, Guided Tooltip, Allocate License (screening, validasi, opsi Target dan Type, Payment dan Cost, Submit, dirty-guard), Edit, Cancel, Resubmit, Approve dan Reject dari Approvals, job sistem (Timeout Auto-Cancel, Activation, Expiry) dan Cancel Term, Role Matrix serta scope data, pencatatan log di Changelog, System Log, Activity Log, dan Allocation Log, format tanggal General Settings, sinkronisasi ke modul konsumen dan notifikasi in-app, defense-in-depth, state tenant (entitas dan Client Suspended atau Expired), konkurensi, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah atau bergantung pada state global: toggle Require Approval for Allocation dan Approval Timeout, harga Product Price, saldo kantong Wallet, format tanggal dan zona waktu General Settings, jam server, status Suspended atau Expired entitas dan Client, capability role, dan flag Guided Tooltip. Spec yang menggeser jam server atau mengubah status entitas memulihkannya di hook `after`. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current; spec yang dimulai dari halaman lain (Approvals, Subscription Detail, Client Detail) berpindah halaman sebagai langkah pertama. Hook `beforeEach` suite juga menjadi jaring pengaman S-09: mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; itu bukan pengganti langkah pemulihan form dirty di spec. `## Prerequisites` spec merujuk pernyataan ini dengan satu baris.
- Flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-license`: hook `before` suite mencatat nilai awal flag lalu menyetelnya `seen` (true) untuk setiap akun UI yang dipakai suite, dan hook `after` memulihkan nilai awal. Spec yang menguji Guided Tooltip mengatur flag sendiri sesudah hook. Kemampuan membaca dan menyetel flag disediakan tim FE/BE.
- Jam: kemampuan mengatur jam server dan jam browser (fixture waktu, nilai absolut) disediakan tim FE/BE. Spec job sistem, boundary SLA, dan Expiry mengaturnya di hook `before` atau langkah eksplisit dan memulihkannya di hook `after`; jam dipulihkan sebelum aksi aktor membuka Activity Log, System Log, atau Changelog (S-09).
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web (bagian 5), sehingga pelaku kedua yang hanya memicu perubahan state memakai sesi API. Kemampuan itu disediakan tim BE/FE dan dinyatakan sekali di sini.
- Fixture backend pemulihan state Pre-setup: baris Pre-setup yang terpaksa berubah (rename Client PT Sejahtera, status Suspended entitas Distributor PT Maju Bersama dan Client Klinik Beku, Gudang Lawas, toggle Require Approval, Approval Timeout, General Settings, capability role, Cancel atau Renew Subscription term, akun nonaktif, alokasi `Active` Asset Control App Pre-setup #53 pada `SUBS-20260105-K2L3M` yang dinonaktifkan spec 128 sebelum blok TC-AC-LA-520 (dipulihkan di hook `after`), binding dan wewenang approver, Product Price dan saldo kantong Wallet, preferensi Setup Column) dipulihkan ke keadaan awal oleh fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC dalam satu spec (S-06, pengecualian 2026-10-30). Efeknya (Last Updated dan entri audit trail) dicatat di `## Prerequisites` spec yang bersangkutan.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status dan 25 entri Changelog) dan Pre-setup #55 (riwayat log lengkap) bersifat baca-saja untuk spec List, Changelog, dan Download; spec yang menulis memakai record seed milik spec sendiri. Data destruktif dipulihkan oleh baseline automation sebelum tiap spec (Catatan TC).
- Email dan password akun Pre-setup #1 sampai #18 dan #56 dirujuk lewat `Fixture.license-allocation-license` (belum ada, disediakan tim FE) dan `Spectra.env.<NAMA>`; tiap spec mendaftarkan akun yang dipakainya di `## Prerequisites`.
