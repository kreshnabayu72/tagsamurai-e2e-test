---
id: TC-GS-USER-E2E-024-edit-user-success
title: Edit user berhasil dan pencatatan Changelog
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-195
  - TC-GS-USER-26
  - TC-GS-USER-196
  - TC-GS-USER-495
coverage:
  web: automated
---

# Edit user berhasil dan pencatatan Changelog

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Budi Santoso" ada, status Activated, Position "Staff", Division "Finance", Last Name "Santoso". Nilai awal ini dicatat
- Position "Supervisor" dan "Manager" ada di master data
- Division "Operations" ada di master data
- Spec ini mengubah nama user "Budi Santoso" menjadi "Budi Kusuma", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Simpan tanpa perubahan

1. Buka Changelog user "Budi Santoso" dan catat jumlah entri
2. Klik row action `Edit` pada baris "Budi Santoso"
3. Klik `[Save]` tanpa mengubah field apa pun
4. Verifikasi toast netral "No changes to save." muncul dan bukan toast sukses
5. Buka Changelog user "Budi Santoso" lagi
6. Verifikasi jumlah entri sama dengan langkah 1 (tidak ada entri baru)

### Edit satu field

7. Klik row action `Edit` pada baris "Budi Santoso"
8. Ubah Position dari "Staff" menjadi "Supervisor"
9. Klik `[Save]`
10. Verifikasi toast "Success, user has been updated." muncul dan perubahan tersimpan langsung
11. Verifikasi baris "Budi Santoso" di User List menampilkan Position "Supervisor"
12. Verifikasi Changelog memuat tepat satu entri baru dengan Field "Position", Old "Staff", New "Supervisor"

### Rename dua kali berturut-turut

13. Klik `Edit` pada "Budi Santoso", ubah Last Name dari "Santoso" menjadi "Wijaya" (First Name tidak diubah), lalu klik `[Save]`
14. Klik `Edit` lagi, ubah Last Name dari "Wijaya" menjadi "Kusuma", lalu klik `[Save]`
15. Buka Changelog user tersebut
16. Verifikasi entri pertama tetap Field "Last Name", Old "Santoso", New "Wijaya" dan tidak berubah menjadi New "Kusuma"
17. Verifikasi entri kedua Field "Last Name", Old "Wijaya", New "Kusuma"
18. Verifikasi tiap edit hanya menghasilkan satu baris dan tidak ada baris untuk First Name

### Edit Position dan Division sekaligus

19. Klik `Edit` pada "Budi Kusuma", ubah Position menjadi "Manager" dan Division menjadi "Operations" dalam satu form, lalu klik `[Save]`
20. Buka Changelog user tersebut
21. Verifikasi Changelog memuat kedua entri: Field "Position" dengan Old "Supervisor" dan New "Manager", serta Field "Division" dengan Old "Finance" dan New "Operations"
22. Verifikasi masing-masing field punya tepat satu entri, tidak ada entri ganda untuk perubahan yang sama
23. Verifikasi field yang tidak diubah (Name, Email, Employee ID, Access, Toggle Active) tidak menghasilkan entri, dan tidak ada entri nyasar ke user lain

## Notes

- `TC-GS-USER-195` sengaja di awal karena tidak mengubah data dan hasilnya (tidak ada entri) dibandingkan dengan jumlah entri sebelum langkah 3.
- Tombol `[Save]` dalam state loading dan disabled selama request (`TC-GS-USER-194`) butuh respons yang ditunda, sehingga dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
- Kegagalan server pada Edit (`TC-GS-USER-32`) juga dicakup spec hanya-FE.
- Sumber TC menulis Changelog Edit sebagai satu baris per field (PRD bagian 8), dengan snapshot Old dan New yang tidak berubah retroaktif.
