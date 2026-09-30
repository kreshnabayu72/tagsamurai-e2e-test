---
id: TC-GS-USER-E2E-034-temporary-user
title: Buat dan ubah Temporary User dengan tanggal expiry
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-66
  - TC-GS-USER-336
  - TC-GS-USER-68
coverage:
  web: automated
---

# Buat dan ubah Temporary User dengan tanggal expiry

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Position dan Division valid ada di master data
- Spec ini membuat user "Bambang Sementara" dengan email unik per run dan tidak menghapusnya. Datanya dibersihkan oleh seeding

## Test Steps

### Validasi tanggal di modal Create

1. Klik `[+ User]` dan isi semua field wajib untuk user "Bambang Sementara"
2. Centang "Set as Temporary User" dan isi Temporary Until dengan tanggal kemarin
3. Klik `[Submit]`
4. Verifikasi inline error "Please select a future date." muncul dan user tidak dibuat

### Buat Temporary User

5. Ganti Temporary Until dengan tanggal 7 hari dari hari ini lalu klik `[Submit]`
6. Verifikasi user "Bambang Sementara" tercipta dan badge "Temporary" tampil pada barisnya
7. Buka Changelog user "Bambang Sementara"
8. Verifikasi ada baris dengan Action "Set Temporary User", Field "Temporary Until", Old "—", New tanggal 7 hari itu, dan Modified By admin yang membuat

### Validasi tanggal di modal Edit

9. Klik row action `Edit` pada "Bambang Sementara"
10. Ganti Temporary Until dengan tanggal kemarin lalu klik `[Save]`
11. Verifikasi inline error "Please select a future date." muncul dan data tidak berubah

### Perpanjang expiry

12. Ganti Temporary Until dengan tanggal 30 hari dari hari ini lalu klik `[Save]`
13. Verifikasi toast "Success, user has been updated." muncul
14. Verifikasi kolom Temporary Until pada "Bambang Sementara" menampilkan tanggal baru dan user tetap Active (tidak ada auto-deactivate prematur)

## Notes

- Pesan "Please select a future date." ada di API (`user-crud.yaml`, `activePeriodUntilPast`), tetapi PRD `user.md` bagian 6 hanya mendefinisikan pesan wajib diisi dan batas tanggal "≥ hari ini". Ketidaksinkronan ini dicatat sebagai `GAP-277`. Spec memakai tanggal kemarin, yang jelas di masa lalu menurut kedua aturan.
- Nonaktif otomatis saat expiry dicakup `TC-GS-USER-E2E-035-temporary-auto-deactivate`, dan reaktivasi user Temporary yang sudah expired dicakup `TC-GS-USER-E2E-036-reaktivasi-temporary-expired`.
