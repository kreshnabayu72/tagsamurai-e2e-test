---
id: TC-GS-ROLE-E2E-056-cross-action-race-concurrency-assign-edit-dan-remove
title: "Penanganan Konflik Konkurensi 2-Aktor: Concurrent Edit CRUD dan Cross-Action Race Assign vs Remove vs Auto-Revert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-111
  - TC-GS-ROLE-317
  - TC-GS-ROLE-318
  - TC-GS-ROLE-319
coverage:
  web: automated
---

# Penanganan Konflik Konkurensi 2-Aktor: Concurrent Edit CRUD dan Cross-Action Race Assign vs Remove vs Auto-Revert

## Prerequisites

- Mode: mock
- Tersedia simulasi race condition 2 sesi admin bersamaan

## Test Steps

1. Buka Detail role pada dua sesi browser admin berbeda (Admin A dan Admin B)
2. Admin A dan Admin B mengedit baris role yang sama secara bersamaan dengan nilai berbeda
3. Verifikasi transaksi kedua ditangani dengan respons 409 Conflict atau optimistic lock yang menampilkan toast peringatan konflik
4. Simulasikan skenario Admin A melakukan Assign Total Control sementara Admin B mengedit cell CRUD target yang sama
5. Verifikasi urutan commit backend tidak merusak integritas tier dan status access_level tetap sinkron dengan pola role
6. Simulasikan skenario Admin A Assign Total Control sementara Admin B me-remove Total Control pada target yang sama
7. Verifikasi state akhir konsisten dan tidak menyisakan baris parsial
8. Simulasikan race condition antara Edit CRUD Auto-Revert dan Remove Role Auto-Revert
9. Verifikasi hanya 1 event Auto-Revert yang tercatat tanpa terjadi duplikasi pencatatan log

## Notes

- Cross-action concurrency race menguji ketahanan invariant tier terhadap interleave transaksi simultan (role.md §9.4 D6).
