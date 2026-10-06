---
id: TC-AC-SU-E2E-027-detail-user-tab-role-group-role-management-dan-assignment-retained
title: "Tab Role Sub-tab Group Role: katalog role, Group Summary Badge, toggle ON retained vs OFF, dan cabut akses group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-74
  - TC-AC-SU-75
  - TC-AC-SU-76
  - TC-AC-SU-77
  - TC-AC-SU-80
  - TC-AC-SU-81
  - TC-AC-SU-82
  - TC-AC-SU-85
coverage:
  web: automated
---

# Tab Role Sub-tab Group Role: katalog role, Group Summary Badge, toggle ON retained vs OFF, dan cabut akses group

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat target pengguna dengan penugasan Group Role aktif dan retained

## Test Steps

### Screening Katalog Group Role dan Group Summary Badge

1. Buka halaman Detail User > Tab Role > Sub-tab `Group Role`
2. Verifikasi seluruh Group Role yang berlaku untuk entitas tampil pada tabel katalog
3. Amati kolom Group pada role yang belum ter-assign, verifikasi menampilkan placeholder `—`
4. Amati kolom Group pada role yang ter-assign ke 4 group, verifikasi menampilkan 2 badge nama group serta badge `"+2 more"`
5. Klik badge `"+2 more"`, verifikasi popup scrollable daftar nama group terbuka

### Toggle ON Retained Assignment dan Toggle OFF

1. Temukan baris Group Role yang sedang OFF namun memiliki assignment tersimpan (retained inactive)
2. Klik switch toggle menjadi ON
3. Verifikasi role langsung aktif memakai data assignment lama TANPA membuka popup penugasan
4. Klik switch toggle kembali menjadi OFF
5. Verifikasi role menjadi nonaktif (`is_active = false`) namun data assignment tetap tersimpan di backend

### Pencabutan Akses Group dan Sinkronisasi 2 Arah

1. Buka popup Assign Group Role pada group role aktif
2. Verifikasi checkbox R (Read) pada tiap baris group berstatus mandatory checked & disabled
3. Klik tombol `[Remove]` pada salah satu baris group di tabel popup lalu klik `[Save]`
4. Verifikasi group tersebut terhapus dari penugasan role ini dan toast sukses muncul
5. Buka menu `Settings > Role & Permission` > Detail Group Role, verifikasi perubahan assignment tercermin sinkron

## Notes

- Penugasan Group Role mendukung retensi konfigurasi saat role dinonaktifkan sementara.
