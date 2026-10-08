---
id: TC-AC-SU-E2E-037-popup-assign-group-role-network-error-5xx-dan-conflict-409
title: "Resiliensi Error Jaringan 5xx dan 409 Conflict pada Popup Assign Group Role"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-97
  - TC-AC-SU-98
  - TC-AC-SU-177
coverage:
  web: automated
---

# Resiliensi Error Jaringan 5xx dan 409 Conflict pada Popup Assign Group Role

## Prerequisites

- Mode: mock
- Login sebagai Total Control
- Modal Assign Group Role siap simpan
- Interceptor mock aktif

## Test Steps

### Resiliensi Error Jaringan 500
1. Lakukan konfigurasi penugasan grup pada modal Assign Group Role
2. Atur interceptor jaringan agar mengembalikan status `500 Internal Server Error`
3. Klik tombol `[Save]`
4. Verifikasi toast error muncul: `"Failed to save group role assignment. Please try again."`
5. Verifikasi modal Assign Group Role TETAP TERBUKA dan seluruh isian input form tetap dipertahankan (tidak terhapus)

### Penanganan Race Condition 409 Conflict
6. Ubah respon interceptor menjadi `409 Conflict` (simulasi peran atau grup telah dimutasi oleh admin lain di latar belakang)
7. Klik tombol `[Save]` kembali
8. Verifikasi toast peringatan muncul: `"Group role data has been modified by another user. Reloading latest data."`
9. Verifikasi modal secara otomatis me-refresh daftar pilihan grup yang relevan

## Notes

Mencegah kehilangan input kerja user saat terjadi gangguan jaringan atau konflik data.
