---
id: TC-GS-USER-E2E-051-isolasi-tenant-dan-scope-entity
title: User entity lain tidak bocor ke User List
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-171
  - TC-GS-USER-392
coverage:
  web: automated
---

# User entity lain tidak bocor ke User List

## Prerequisites

Spec ini dijalankan untuk setiap entity pada tabel. Langkahnya identik, hanya akun login yang berbeda.

Entity yang diuji:

| Entity | Akun | Yang tidak boleh tampil |
|---|---|---|
| Entity A (Client) | Total Control pada entity A | User milik entity B |
| Entity B (Client) | Total Control pada entity B | User milik entity A |
| Distributor | Total Control pada entity Distributor | Staff milik Partner downstream |

- Entity A dan B masing-masing punya user dengan nama unik yang tidak sama dengan user entity lain: "User Entity A" dan "User Entity B"
- Entity Distributor punya minimal satu Partner downstream yang punya staff User sendiri: "Staff Partner Downstream"
- Nama akun dan entity disiapkan tim FE
- Spec ini hanya membaca data dan mencoba satu Create yang ditolak, jadi tidak butuh cleanup

## Test Steps

Lakukan langkah 1–5 untuk setiap entity pada tabel.

1. Login sebagai Total Control pada entity yang diuji, lalu buka User List
2. Verifikasi User List hanya menampilkan user milik entity itu sendiri
3. Cari nama user dari entity lain (dari kolom "Yang tidak boleh tampil") lewat kotak Search
4. Verifikasi hasil pencarian kosong dan user dari entity lain tidak bocor ke tabel
5. Untuk entity Client: klik `[+ User]`, isi field wajib dengan email milik user dari entity lain, lalu klik `[Submit]`, dan verifikasi inline error "Email already exists" muncul (email unik global lintas entity) tanpa data user entity lain tersingkap

## Notes

- Isolasi tenant ditegakkan di sisi data, bukan hanya di tampilan (D4 scope entitas). Langkah 5 membuktikan email unik global tanpa membuka isi user entity lain.
- Distributor tidak menampilkan staff Partner downstream, murni per entity tanpa agregasi (mirror General Settings bagian 1.4a, bukan pola agregasi Activity Log Admin Console).
- Cara skrip menjalankan banyak entity diputuskan di tahap script.
