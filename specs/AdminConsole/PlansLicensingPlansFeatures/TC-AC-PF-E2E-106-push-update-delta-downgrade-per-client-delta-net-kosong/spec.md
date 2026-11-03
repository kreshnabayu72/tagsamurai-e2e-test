---
id: TC-AC-PF-E2E-106-push-update-delta-downgrade-per-client-delta-net-kosong
title: "Push Update: Delta Downgrade, Eligibilitas per Client, dan Delta Net Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-268
  - TC-AC-PF-269
  - TC-AC-PF-270
coverage:
  web: automated
---

# Push Update: Delta Downgrade, Eligibilitas per Client, dan Delta Net Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan P (Pre-setup #28): custom plan Principal `Paket Turun` v3 (v1 Group count 25 dan Asset Name cap 50; v2 Group count 3; v3 Asset Name cap 500) dengan `PT Turun Satu` Active v1 dan `PT Turun Dua` Active v2; `Paket Revert` v3 (v1 Scheduled reports 5; v2 Scheduled reports 1; v3 Scheduled reports 5) dengan `PT Revert Satu` Active v1. Dataset hanya dibaca; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan P) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data (seluruh blok hanya membaca). Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-268: Client dengan delta downgrade: Push Update tidak tampil, badge Outdated dan icon peringatan

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Plan Detail `Paket Turun`
3. Klik Tab Assigned Clients
4. Verifikasi Baris `PT Turun Satu` menampilkan badge `Outdated` didampingi icon peringatan
5. Arahkan kursor ke icon peringatan baris `PT Turun Satu`
6. Verifikasi Tooltip icon: "This client cannot receive a push update — the current plan version reduces one or more features. Manage via Allocation > Client Subscription."
7. Buka Overlay Row Action `PT Turun Satu`
8. Verifikasi Overlay Row Action hanya memuat `Detail` (tanpa partial push per field)
9. Tutup Overlay Row Action

### TC-AC-PF-269: Eligibilitas dihitung per client

10. Buka Overlay Row Action `PT Turun Satu`
11. Verifikasi Overlay Row Action `PT Turun Satu` hanya memuat `Detail`
12. Tutup Overlay Row Action
13. Buka Overlay Row Action `PT Turun Dua`
14. Verifikasi Overlay Row Action `PT Turun Dua` memuat `Detail` dan `Push Update`
15. Tutup Overlay Row Action

### TC-AC-PF-270: Delta net kosong: baris tetap Outdated, Push Update Hidden

16. Kembali ke Plans List tab Custom sub-tab Active
17. Buka Plan Detail `Paket Revert`
18. Klik Tab Assigned Clients
19. Verifikasi Baris `PT Revert Satu` menampilkan badge `Outdated`
20. Arahkan kursor ke badge `Outdated` baris `PT Revert Satu`
21. Verifikasi Tooltip badge "No feature changes"
22. Buka Overlay Row Action `PT Revert Satu`
23. Verifikasi Overlay Row Action hanya memuat `Detail` (tabel diff tidak dapat dibuka)
24. Tutup Overlay Row Action

## Notes

- Plan Detail `Paket Turun` dan Tab Assigned Clients dibuka satu kali dan dipakai ulang oleh TC-AC-PF-269 (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mengarahkan kursor ke icon dan badge agar tooltip muncul, dan menutup Overlay Row Action.
- Temuan untuk QA: TC-AC-PF-270 Expected butir b menyebut tabel diff tidak dapat dibuka; ditulis dalam satu `Verifikasi` bersama Overlay Row Action hanya `Detail` karena merupakan kesimpulan yang tidak teramati terpisah (S-03).
