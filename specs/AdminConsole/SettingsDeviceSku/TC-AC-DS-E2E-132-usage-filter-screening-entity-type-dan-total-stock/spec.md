---
id: TC-AC-DS-E2E-132-usage-filter-screening-entity-type-dan-total-stock
title: "Filter Usage: Screening, Opsi Entity Type, Entity Type Dua Badge, dan OR"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-446
  - TC-AC-DS-447
  - TC-AC-DS-448
  - TC-AC-DS-560
coverage:
  web: automated
---

# Filter Usage: Screening, Opsi Entity Type, Entity Type Dua Badge, dan OR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris dan jaringan entitas (#32, #24): `PT Arunika Prima` (Principal) 55, `PT Cakra Distribusi` (Distributor) 25, `PT Delta Retail` (Client) 5, `PT Mitra Lintas Nusa` (Distributor dan Client) 20, `PT Surya Logistik` (Client) 15. Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Verifikasi tabel Usage memuat sedikitnya satu baris

### TC-AC-DS-446: Screening Filter Panel Usage: field, placeholder, dan tombol

4. Klik ikon Filter pada popup
5. Verifikasi Filter Panel popup tampil
6. Verifikasi field berurutan: Entity Type "All entity types", lalu Total Stock "Min" serta "Max"
7. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-DS-447: Isi opsi Filter Entity Type berasal dari data tabel Usage

8. Klik field Entity Type
9. Verifikasi opsi memuat `Principal`, `Distributor`, dan `Client`
10. Verifikasi tidak ada opsi `Partner`

### TC-AC-DS-448: Filter Entity Type mencocokkan salah satu badge termasuk baris dengan dua badge

11. Pada field Entity Type pilih `Distributor`
12. Klik `[Apply]` pada Filter Panel popup
13. Verifikasi Entity Type `Distributor` menampilkan `PT Cakra Distribusi` dan `PT Mitra Lintas Nusa` (salah satu badge Distributor)
14. Klik `[Clear Field]`, pilih Entity Type `Client`, klik `[Apply]`
15. Verifikasi Entity Type `Client` menampilkan `PT Delta Retail`, `PT Mitra Lintas Nusa`, dan `PT Surya Logistik`

### Pemulihan state antar TC

16. Klik `[Clear Field]`

### TC-AC-DS-560: Filter Entity Type Usage dengan beberapa opsi digabung OR

17. Pada field Entity Type pilih `Principal` dan `Client`
18. Klik `[Apply]` pada Filter Panel popup
19. Verifikasi tabel memuat baris Entity Type `Principal` atau `Client`: `PT Arunika Prima`, `PT Delta Retail`, `PT Mitra Lintas Nusa`, dan `PT Surya Logistik`
20. Verifikasi `PT Cakra Distribusi` (hanya `Distributor`) tidak tampil

### Pemulihan state akhir

21. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup popup dengan ikon close `[✕]`

## Notes

- Langkah 1 sampai 3 adalah pembuka bersama (popup `HHR-ARC-100` dibuka sekali). Langkah 3 adalah pembanding generik sebelum asersi filter (8b butir 2).
- Langkah penghubung tanpa `Verifikasi`: langkah 16 dan 21 (membersihkan filter, S-03, S-09). Langkah 14 mengikuti TC 448 langkah 6 apa adanya (`[Clear Field]` langsung setelah `[Apply]`).
- Expected 446 butir a dan b ditulis langkah 6 dan 7; 447 butir a dan b langkah 9 dan 10; 448 butir a langkah 13 dan butir b langkah 15; 560 butir a dan b langkah 19 dan 20.
- Rentang Total Stock Min-Max diuji di spec 133 (TC-AC-DS-449 dan 571).
- Temuan untuk QA:
  - S-15: TC 448 langkah 6 mengklik `[Clear Field]` tepat setelah `[Apply]` tanpa menyebut apakah Filter Panel masih terbuka setelah Apply; spec mengikuti TC.
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
