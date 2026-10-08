---
id: TC-GS-ACTLOG-E2E-013-tenant-scoping-dan-isolasi-data
title: "Isolasi Data Antar-Tenant dan Entitas (Client, Principal, Distributor, Partner) Tanpa Masking"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-35
  - TC-GS-ACTLOG-36
  - TC-GS-ACTLOG-37
  - TC-GS-ACTLOG-127
coverage:
  web: automated
---

# Isolasi Data Antar-Tenant dan Entitas (Client, Principal, Distributor, Partner) Tanpa Masking

## Prerequisites

- Client Alfa dan Client Beta memiliki entri log masing-masing (misal admin Client Beta: 'Rina Marlina')
- Entitas Principal Satu, Distributor Dua, dan Partner Tiga memiliki log masing-masing
- Akun login Total Control dan Read Only untuk masing-masing entitas

## Test Steps

### Isolasi Data Antar-Client
1. Login sebagai Total Control Client Alfa, buka Tab Session.
2. Cari kata kunci 'Rina' di kotak Search, verifikasi tidak ada baris yang ditemukan.
3. Buka dropdown filter User, verifikasi nama 'Rina Marlina' tidak ada dalam daftar opsi.
4. Buka Tab User Action, cari 'Rina', verifikasi tidak ada data milik Client Beta yang tampil.
### Isolasi Entitas Principal, Distributor, dan Partner
5. Login sebagai Total Control Principal Satu, verifikasi hanya log milik Principal Satu yang tampil.
6. Login sebagai Total Control Distributor Dua, verifikasi hanya log milik Distributor Dua yang tampil.
7. Login sebagai Total Control Partner Tiga, verifikasi hanya log milik Partner Tiga yang tampil.
### Ketiadaan Masking Field Audit
8. Pada Tab Session Client Alfa, amati baris log pengguna 'John Doe'.
9. Verifikasi seluruh field audit (IP Address, Note, Employee ID, Position, Division) ditampilkan penuh tanpa masking bintang (***) baik untuk role Total Control maupun Read Only.
### Isolasi Berkas Ekspor Download
10. Unduh berkas CSV dari Tab Session dan Tab User Action Client Alfa.
11. Buka kedua berkas, cari nama 'Rina', verifikasi berkas tidak memuat log milik Client Beta.

## Notes

- Sesuai ACTLOG-LOGIC-03 log ter-scope ketat ke entitas aktif dan field audit tampil penuh untuk mendukung investigasi keamanan.
