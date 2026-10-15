---
id: TC-AC-SU-E2E-035-popup-assign-group-role-save-put-replace-lifecycle
title: "Assign Group Role: Alur Penyimpanan Save Replace PUT dan Verifikasi No-Op"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-78
  - TC-AC-SU-96
  - TC-AC-SU-250
  - TC-AC-SU-257
coverage:
  web: automated
---

# Assign Group Role: Alur Penyimpanan Save Replace PUT dan Verifikasi No-Op

## Prerequisites

- Login sebagai Total Control
- Membuka modal penugasan peran grup untuk user target

## Test Steps

### Alur Penyimpanan Penugasan Baru (PUT Replace)
1. Buka Detail User > tab `Role` > sub-tab `Group Role`
2. Klik toggle switch pada peran grup yang belum aktif (toggle ON dari posisi kosong)
3. Verifikasi modal `Assign Group Role` terbuka secara otomatis
4. Tambahkan grup `"Cabang Surabaya"` dan pilih role `"Operator"`
5. Klik tombol `[Save]` pada modal
6. Verifikasi request `PUT /users/{id}/group-roles` terkirim dengan payload lengkap menggantikan (replace) daftar penugasan lama
7. Verifikasi toast sukses muncul: `"Group roles assigned successfully."`
8. Verifikasi toggle peran kini berada di posisi ON dan badge summary menampilkan jumlah grup yang baru

### Verifikasi Logika No-Op Saat Form Bersih
9. Buka kembali modal Assign Group Role untuk user tersebut
10. Tanpa mengubah satu pun pilihan grup atau peran, langsung klik tombol `[Save]`
11. Verifikasi sistem mendeteksi state identik (clean state) dan melakukan no-op tanpa mengirim payload mutasi redundan ke backend

## Notes

Memastikan integritas payload mutasi peran grup dan efisiensi network.
