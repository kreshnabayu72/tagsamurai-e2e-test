---
id: TC-AC-CS-E2E-103-list-state-preservation-memori-per-tab
title: "List State Preservation: Memori per Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-33
  - TC-AC-CS-34
  - TC-AC-CS-56
coverage:
  web: automated
---

# List State Preservation: Memori per Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History; Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Kelas volume data (e): dataset Pre-setup #82 (halaman 2 pada tab `Current` dan jumlah baris yang memuat `Apotek`, `Optik`, dan `Sejahtera`).

## Test Steps

### TC-AC-CS-33: Kunjungan pertama ke tab History memuat isi tab itu mulai dari halaman 1

1. Klik pagination halaman `2` pada tab `Current`
2. Klik tab `History`
3. Verifikasi tabel menampilkan sedikitnya satu baris
4. Verifikasi isi tabel hanya baris History
5. Verifikasi paginasi tab `History` ada di halaman 1

### TC-AC-CS-34: Kembali ke tab yang sudah pernah dikunjungi memulihkan state tab itu

6. Klik tab `Current`, lalu ketik Search `Apotek`, tekan Enter
7. Klik tab `History`, lalu ketik Search `Optik`, tekan Enter
8. Klik tab `Current`
9. Verifikasi kolom Search tab `Current` berisi `Apotek`
10. Verifikasi tabel tab `Current` menampilkan sedikitnya satu baris
11. Verifikasi seluruh baris tab `Current` yang tampil memuat `Apotek`
12. Verifikasi state tab `History` (Search `Optik`) tidak memengaruhi tab `Current`
13. Klik tab `History`
14. Verifikasi kolom Search tab `History` berisi `Optik`
15. Verifikasi tabel tab `History` menampilkan sedikitnya satu baris
16. Verifikasi seluruh baris tab `History` yang tampil memuat `Optik`
17. Klik `(←)` pada kotak Search tab `History`, lalu klik tab `Current` dan klik `(←)` pada kotak Search

### TC-AC-CS-56: Klik crumb Client Subscription pada Detail kembali ke List dengan state terjaga

18. Ketik Search `Sejahtera`, tekan Enter, lalu pindah ke halaman `2` pada tab `Current`
19. Klik satu baris untuk membuka Detail
20. Verifikasi crumb pertama `Allocation` dan crumb terakhir `Detail` bukan link
21. Klik crumb `Client Subscription` pada Breadcrumb
22. Verifikasi List kembali ke tab `Current`
23. Verifikasi Search `Sejahtera` dipertahankan
24. Verifikasi sort dan filter dipertahankan
25. Verifikasi tabel berada di halaman 2
26. Klik `(←)` pada kotak Search

## Notes

- TC-AC-CS-33 dan 34 berurutan (Dependensi TC-AC-CS-34 pada TC-AC-CS-33).
- Langkah penghubung (S-03): langkah `(←)` yang mengosongkan Search di akhir blok TC-AC-CS-34 dan TC-AC-CS-56 (bagian 8b butir 9), dan klik tab.
- Asersi universal ("hanya baris History", "seluruh baris memuat") didahului `Verifikasi` sedikitnya satu baris pada permukaan yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-33 Expected a ("Isi tabel hanya baris History") tidak menyebut tanda baris History; spec memakai status data mati tab `History`.
  - TC-AC-CS-56 butir Langkah Uji ke-1 menyebut Search `Sejahtera` dan halaman 2 sekaligus; jumlah baris Pre-setup #82 yang memuat `Sejahtera` tidak dinyatakan sehingga halaman 2 belum tentu tersedia.
  - TC-AC-CS-56 Expected b menyebut sort dan filter dipertahankan padahal Langkah Uji tidak mengatur sort maupun filter; spec mengasersi keduanya sebagai keadaan bawaan.
